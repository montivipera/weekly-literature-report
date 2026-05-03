"""Boolean query parser and per-source serializer.

The user writes one Boolean expression per category in `config.yaml`. We parse
that into an AST so we can:

  1. Serialize it into the syntax each source expects (PubMed/arXiv have rich
     Boolean support; Crossref and Semantic Scholar do not, so we approximate).
  2. Run client-side filtering for sources without server-side Boolean (bioRxiv)
     and as a safety filter when we don't trust the source's interpretation.

Grammar (case-insensitive operators):

    expr   := or_expr
    or_expr  := and_expr ( OR and_expr )*
    and_expr := not_expr ( (AND | <implicit-and>) not_expr )*
    not_expr := NOT atom | atom
    atom   := '(' expr ')' | quoted | term

A bare adjacency (e.g. ``foo bar``) is treated as implicit AND.
"""

from __future__ import annotations

import re
from dataclasses import dataclass
from typing import List, Optional, Union


# ---------------------------------------------------------------------------
# AST nodes
# ---------------------------------------------------------------------------


@dataclass
class Term:
    text: str
    quoted: bool = False

    def __repr__(self) -> str:
        return f'Term({self.text!r}, quoted={self.quoted})'


@dataclass
class Not:
    child: "Node"


@dataclass
class And:
    children: List["Node"]


@dataclass
class Or:
    children: List["Node"]


Node = Union[Term, Not, And, Or]


# ---------------------------------------------------------------------------
# Tokenizer
# ---------------------------------------------------------------------------


_TOKEN_RE = re.compile(
    r"""
    \s+                            |   # whitespace
    (?P<lparen>\()                 |
    (?P<rparen>\))                 |
    (?P<quoted>"[^"]*")            |
    (?P<word>[^\s()"]+)
    """,
    re.VERBOSE,
)


@dataclass
class Token:
    kind: str   # 'AND' | 'OR' | 'NOT' | 'LPAREN' | 'RPAREN' | 'TERM'
    value: str
    quoted: bool = False


def _tokenize(query: str) -> List[Token]:
    tokens: List[Token] = []
    pos = 0
    while pos < len(query):
        m = _TOKEN_RE.match(query, pos)
        if not m:
            raise ValueError(f"Cannot tokenize query at position {pos}: {query!r}")
        if m.group("lparen"):
            tokens.append(Token("LPAREN", "("))
        elif m.group("rparen"):
            tokens.append(Token("RPAREN", ")"))
        elif m.group("quoted"):
            raw = m.group("quoted")
            tokens.append(Token("TERM", raw[1:-1], quoted=True))
        elif m.group("word"):
            w = m.group("word")
            up = w.upper()
            if up in ("AND", "OR", "NOT"):
                tokens.append(Token(up, up))
            else:
                tokens.append(Token("TERM", w))
        # else: whitespace match — skip
        pos = m.end()
    return tokens


# ---------------------------------------------------------------------------
# Parser (recursive descent)
# ---------------------------------------------------------------------------


class _Parser:
    def __init__(self, tokens: List[Token]):
        self.tokens = tokens
        self.pos = 0

    def peek(self) -> Optional[Token]:
        return self.tokens[self.pos] if self.pos < len(self.tokens) else None

    def consume(self) -> Token:
        t = self.tokens[self.pos]
        self.pos += 1
        return t

    def parse(self) -> Node:
        node = self.parse_or()
        if self.peek() is not None:
            raise ValueError(f"Unexpected token {self.peek()!r}")
        return node

    def parse_or(self) -> Node:
        children: List[Node] = [self.parse_and()]
        while self.peek() is not None and self.peek().kind == "OR":
            self.consume()
            children.append(self.parse_and())
        return children[0] if len(children) == 1 else Or(children)

    def parse_and(self) -> Node:
        children: List[Node] = [self.parse_not()]
        while True:
            t = self.peek()
            if t is None:
                break
            if t.kind == "AND":
                self.consume()
                children.append(self.parse_not())
                continue
            # Implicit AND between adjacent atoms
            if t.kind in ("TERM", "LPAREN", "NOT"):
                children.append(self.parse_not())
                continue
            break
        return children[0] if len(children) == 1 else And(children)

    def parse_not(self) -> Node:
        t = self.peek()
        if t is not None and t.kind == "NOT":
            self.consume()
            return Not(self.parse_atom())
        return self.parse_atom()

    def parse_atom(self) -> Node:
        t = self.peek()
        if t is None:
            raise ValueError("Unexpected end of query")
        if t.kind == "LPAREN":
            self.consume()
            inner = self.parse_or()
            close = self.peek()
            if close is None or close.kind != "RPAREN":
                raise ValueError("Missing closing parenthesis")
            self.consume()
            return inner
        if t.kind == "TERM":
            self.consume()
            return Term(t.value, quoted=t.quoted)
        raise ValueError(f"Unexpected token: {t!r}")


def parse_query(query: str) -> Node:
    """Parse a Boolean query string into an AST."""
    tokens = _tokenize(query)
    if not tokens:
        raise ValueError("Empty query")
    return _Parser(tokens).parse()


# ---------------------------------------------------------------------------
# Serializers
# ---------------------------------------------------------------------------


def _quote_phrase(t: Term) -> str:
    if t.quoted or " " in t.text:
        return f'"{t.text}"'
    return t.text


def to_pubmed(node: Node) -> str:
    """Serialize for the PubMed E-utilities `term=` parameter.

    We tag each term with [Title/Abstract] so retrieval focuses on relevant
    fields. Operators are uppercase (PubMed requires that)."""

    def emit(n: Node) -> str:
        if isinstance(n, Term):
            return f'{_quote_phrase(n)}[Title/Abstract]'
        if isinstance(n, Not):
            return f'NOT {emit(n.child)}'
        if isinstance(n, And):
            return "(" + " AND ".join(emit(c) for c in n.children) + ")"
        if isinstance(n, Or):
            return "(" + " OR ".join(emit(c) for c in n.children) + ")"
        raise TypeError(type(n))

    return emit(node)


def to_arxiv(node: Node) -> str:
    """Serialize for the arXiv `search_query` parameter.

    Each term is prefixed with `all:`. Phrases are quoted. Boolean operators
    are uppercase (arXiv requires that)."""

    def emit(n: Node) -> str:
        if isinstance(n, Term):
            return f'all:{_quote_phrase(n)}'
        if isinstance(n, Not):
            inner = emit(n.child)
            return f'ANDNOT {inner}'  # arXiv uses ANDNOT
        if isinstance(n, And):
            return "(" + " AND ".join(emit(c) for c in n.children) + ")"
        if isinstance(n, Or):
            return "(" + " OR ".join(emit(c) for c in n.children) + ")"
        raise TypeError(type(n))

    out = emit(node)
    out = out.replace("AND ANDNOT", "ANDNOT")
    return out


def to_bibliographic(node: Node) -> str:
    """Best-effort flat string for sources without true Boolean support.

    Used by Crossref's ``query.bibliographic`` and Semantic Scholar's ``query``.
    Both treat the query as a relevance-ranked free-text search, so we extract
    positive terms and join them with spaces. NOT branches are dropped; OR
    branches contribute all alternatives. We re-apply the AST as a client-side
    filter to keep results faithful to the user's intent.
    """
    terms: List[str] = []

    def collect(n: Node, polarity: bool) -> None:
        if isinstance(n, Term):
            if polarity:
                terms.append(_quote_phrase(n))
        elif isinstance(n, Not):
            collect(n.child, not polarity)
        elif isinstance(n, And) or isinstance(n, Or):
            for c in n.children:
                collect(c, polarity)

    collect(node, True)
    return " ".join(terms)


# ---------------------------------------------------------------------------
# Client-side evaluation
# ---------------------------------------------------------------------------


def matches(node: Node, text: str) -> bool:
    """Evaluate the AST against a haystack of text. Case-insensitive.

    Phrases must match as contiguous substrings (after whitespace collapse).
    Bare terms match as case-insensitive substrings on word boundaries when
    possible, falling back to plain substring."""
    haystack = re.sub(r"\s+", " ", (text or "").lower())

    def _term_match(t: Term) -> bool:
        needle = t.text.lower().strip()
        if not needle:
            return True
        if t.quoted or " " in needle:
            return needle in haystack
        # Word-boundary match for single tokens
        return re.search(rf"(?<![a-z0-9]){re.escape(needle)}(?![a-z0-9])", haystack) is not None

    def emit(n: Node) -> bool:
        if isinstance(n, Term):
            return _term_match(n)
        if isinstance(n, Not):
            return not emit(n.child)
        if isinstance(n, And):
            return all(emit(c) for c in n.children)
        if isinstance(n, Or):
            return any(emit(c) for c in n.children)
        raise TypeError(type(n))

    return emit(node)


def filter_articles(node: Node, articles, text_fields=("title", "abstract")):
    """Return only articles whose combined ``text_fields`` satisfy the AST."""
    out = []
    for a in articles:
        text = " ".join((getattr(a, f, "") or "") for f in text_fields)
        if matches(node, text):
            out.append(a)
    return out
