# DOI ledger: <paper short title> (`<slug>`)
derives-from: search-log.md@<short-commit>, scan-notes.md@<short-commit>
Updated: <YYYY-MM-DD> · reference rows: <n> · claim rows: <n> · refs to be cited at `SUPPORT-CHECKED`: <n>/<n> · plan tag date: <YYYY-MM-DD | no plan>

The ledger has three linked tables:
- (a) search rows `S..` record what was searched;
- (b) reference rows `R..` record whether a source exists, matches its metadata and has been retracted;
- (c) claim rows `CL..` record whether a passage supports a claim.

Rows are appended and never deleted; only status cells change. EXAMPLE rows show the format only: their dates and statuses are illustrative, not checks that were run. Delete them when the paper's ledger starts.

## Rules
1. Existence ≠ metadata accuracy ≠ claim support. A DOI that resolves is only `RESOLVED`, and drafts cite only `SUPPORT-CHECKED` rows [D1, D4, D16].
2. Retrieval, never memory: every R row traces to an S row (a database or MCP tool hit). No reference is ever typed from recall [A21, D5].
3. Regional, national, local and post-2020 references get a human spot-check before `SUPPORT-CHECKED`, with the human named as verifier [D4, D9].
4. A summary (layer synthesis, NotebookLM note or agent report) may cite only row IDs (`R..`, `CL..`), never another summary [D19, D21].
5. The verifier is never the drafting model. Claim support comes only from full text (`fulltext: yes`), never from an abstract [D14, D18, D20].
6. Every R row gets a retraction check before `METADATA-OK`. A retracted source becomes `RETRACTED` and is never cited as support [F29, D17].

## Status ladder
`UNRESOLVED` → `RESOLVED` → `METADATA-OK` → `SUPPORT-CHECKED`, with two exits: `RETRACTED` and `NOT-CITABLE`.
- `UNRESOLVED`: the row was entered from a search hit but not yet looked up.
- `RESOLVED`: the DOI or PMID resolves in Crossref, OpenAlex, PubMed or an MCP tool.
- `METADATA-OK`: authors, year, title, venue and volume/pages match the resolver record, and the retraction check is clean.
- `SUPPORT-CHECKED`: every claim row that cites this reference is `SUPPORT-CHECKED`.
- `RETRACTED`: a retraction or withdrawal notice was found.
- `NOT-CITABLE`: there is no stable record, the item is an AI output, or support could not be confirmed.

Claim rows use three of these values: `UNRESOLVED` (not checked yet), `SUPPORT-CHECKED` (the passage supports the claim as worded) and `NOT-CITABLE` (the passage does not support it, or the row has `fulltext: no`).

## (a) Search-and-consultation log
A search is `consulted: before-results` if it ran before the first outcome model (compare its date with the plan tag date). Otherwise it is `consulted: after-results`.
Stage 02 rows are copied from search-log.md, and stage 08 appends its own.
| S-ID | Date | Stage · layer | Database or tool | Search string (verbatim) | Filters | Hits | Screened → R rows | Consulted |
|---|---|---|---|---|---|---|---|---|
| S<nn> | <YYYY-MM-DD> | <02 \| 08> · <global \| regional \| national \| local> | <database or MCP tool> | <exact string as run> | <years, language, type> | <n> | <n> → <R-ids> | `consulted: <before-results \| after-results>` |
| EXAMPLE S01 | 2026-10-06 | 02 · global | OpenAlex | ("hydroperiod" OR "pond permanence") AND (Odonata OR dragonfl*) AND richness | 2000–2026; articles | 212 | 31 → R01 | `consulted: before-results` |
| EXAMPLE S02 | 2026-11-20 | 08 · national | Scopus | (wetland OR marsh) AND amphibian* AND "<country>" | none | 47 | 12 → R02 | `consulted: after-results` |

## (b) Reference rows
| ID | Source (first author, year, venue) | DOI | Resolver | Resolve date | Metadata match | Retraction check | Fulltext | Consulted | Status |
|---|---|---|---|---|---|---|---|---|---|
| R<nn> | <author, year, venue> | <10.xxxx/...> | <Crossref \| OpenAlex \| PubMed \| MCP: tool name> | <YYYY-MM-DD> | <yes \| no: field(s) wrong> | <none found YYYY-MM-DD via <source> \| retracted> | `fulltext: <yes \| no>` | `consulted: <before-results \| after-results>` | <status> |
| EXAMPLE R01 | Zuur & Ieno 2016, Methods Ecol Evol | 10.1111/2041-210x.12577 | Crossref | <YYYY-MM-DD> | yes | none found <YYYY-MM-DD> | `fulltext: yes` | `consulted: before-results` | `SUPPORT-CHECKED` |
| EXAMPLE R02 | Fraser et al. 2018, PLOS ONE | 10.1371/journal.pone.0200303 | OpenAlex | <YYYY-MM-DD> | yes | none found <YYYY-MM-DD> | `fulltext: no` | `consulted: after-results` | `METADATA-OK` (no claim may cite it until the full text is read) |

## (c) Claim-support rows
| Claim ID | Claim (as worded in the draft) | Ref ID | Verbatim quote | Page or section | Verifier | Date | Status |
|---|---|---|---|---|---|---|---|
| CL<nn> | <one sentence> | R<nn> | "<copied exactly from the full text>" | <p. n \| §n.n \| Table n> | <citation-verifier (agent) \| human: initials> | <YYYY-MM-DD> | <status> |
| EXAMPLE CL01 | Data exploration (outliers, collinearity, dependence) should come before model fitting. | R01 | "<verbatim sentence from the R01 full text>" | <§n> | citation-verifier (agent) | <YYYY-MM-DD> | `SUPPORT-CHECKED` |
| EXAMPLE CL02 | About half of surveyed ecologists reported presenting an unexpected finding as if it had been hypothesised. | R02 | none (abstract only) | none | citation-verifier (agent) | <YYYY-MM-DD> | `UNRESOLVED` (needs `fulltext: yes`) |

## AI-summary provenance list (every row `NOT-CITABLE`)
These outputs are for orientation only, and no draft sentence may rest on them. A fact first found here can be cited only after it has its own R and CL rows [D19, D24, D25, D36].
| AI-ID | Tool (name, version or model ID) | Date | Scope (sources loaded; question asked) | Output kept at | Used for | Status |
|---|---|---|---|---|---|---|
| AI<nn> | <tool> | <YYYY-MM-DD> | <n sources, layer; prompt> | <path> | <which S searches or outline it prompted> | `NOT-CITABLE` |
| EXAMPLE AI01 | NotebookLM | 2026-11-18 | 34 PDFs, regional layer; "What drives amphibian decline in <region> wetlands?" | ai01-notebooklm-regional.md | suggested search S02 | `NOT-CITABLE` |
| EXAMPLE AI02 | claude-sonnet-5-5 (lit-extractor) | 2026-11-21 | layer synthesis built from R02–R12 | ai02-national-synthesis.md | outline of Introduction paragraph 2; it cites only R and CL IDs | `NOT-CITABLE` |

## Disclosure fields
Fill these at stage 07 and re-check them at stage 10 against the live policy page. Policy wording in our research comes from search snippets, so treat it as UNVERIFIED [D27–D32].
- Target journal and AI policy: <journal> · <policy URL> · live page re-read on <YYYY-MM-DD>
- AI tools used: <name and model ID or version of each tool, including NotebookLM>
- Used for what: <data inventory \| analysis code \| literature extraction \| citation checks \| drafting \| language editing>. Not used for: <research figures [D30] \| scientific judgements, which stay with the authors>
- Human oversight: <who checked which outputs>. The authors take full responsibility [D26, D31].
- Where disclosed: <Methods \| Acknowledgements \| declaration section before References \| cover letter>, as the target journal requires [D27, D28, D30, D32]
- Reference declaration, used only if every cited row is `SUPPORT-CHECKED`: "All references were checked to exist, to be cited accurately and to support the claims made." [D17]
