# DOI ledger: <paper short title> (`<slug>`)
derives-from: question-map.md@<short-commit>
Updated: <YYYY-MM-DD> · Q rows: <n> · R rows: <n> · CL rows: <n> · plan tag date: <YYYY-MM-DD | no plan>
to-be-cited: <N> | SUPPORT-CHECKED: <n> | other: <n> | checked <YYYY-MM-DD>

The ledger has three linked tables:
- (a) search rows `Q<nn>` record what was searched;
- (b) reference rows `R<nn>` record whether a source exists, matches its metadata and has been retracted;
- (c) claim-support rows `CL<nn>` record whether a passage supports a claim as worded.

It also holds the layer syntheses, the to-be-cited list, the AI-summary provenance list and the disclosure checklist.

Rows are appended and never deleted; only verification cells change. Cells hold the bare values shown in each header. In prose, `risk: high` means the risk cell reads `high`; the same holds for `fulltext:` and `consulted:`. EXAMPLE rows show the format only: their dates and statuses are illustrative, not checks that were run. Delete them when the paper's ledger starts.

## Rules
1. Existence ≠ metadata accuracy ≠ claim support. An R row stops at `METADATA-OK`; only a CL row reaches `SUPPORT-CHECKED` [D1, D4, D16].
2. Drafts cite CL rows only, as `[ledger: CL12, CL15]`, and only at `SUPPORT-CHECKED`. The reference list is generated from the R rows of the cited CL rows, and each of those R rows is `METADATA-OK`.
3. Retrieval, never memory: every R row is named under "rows kept" of a Q row (a database or MCP tool hit). No reference is ever typed from recall [A21, D5].
4. Human check: every `risk: high` row, plus a sample of ≥10 rows or 10% of the rest. The human is named in the verifier cell [D4, D9]. `risk: high` marks the regional, national and local layers.
5. A summary (layer synthesis, NotebookLM note or agent report) may cite only row IDs, never another summary [D19, D21].
6. The verifier is never the drafting or extracting model. Claim support comes only from full text (R row `fulltext: yes`), never from an abstract [D14, D18, D20].
7. The retraction check runs before `METADATA-OK` is set. A retracted source becomes `RETRACTED` and is never cited as support [F29, D17].
8. Opus agents (drafter, critic) read a grep-extracted slice of this file (the CL rows named in the skeleton or the question map, plus their R rows), never the whole ledger.

## Status ladders
R rows: `UNRESOLVED` → `RESOLVED` → `METADATA-OK` (terminal), with two exits: `RETRACTED` and `NOT-CITABLE`.
- `UNRESOLVED`: entered from a search hit, not yet looked up.
- `RESOLVED`: the DOI or PMID resolves in Crossref, OpenAlex, PubMed or an MCP tool.
- `METADATA-OK`: the retraction check reads `clear`, then authors, year, title and venue match the resolver record.
- `RETRACTED`: a retraction or withdrawal notice was found. To discuss a retraction, cite the notice as its own R row.
- `NOT-CITABLE`: no stable record, an AI output, or the DOI resolves to a different work.

CL rows: `UNRESOLVED` → `SUPPORT-CHECKED`, or `NOT-CITABLE`. `SUPPORT-CHECKED` needs its R row at `METADATA-OK` with `fulltext: yes`, and the quote found word for word at its page or section, supporting the claim as worded.

## (a) Search log
Stage 08 copies the stage 02 Q rows from search-log.md with IDs unchanged and appends its own. A search is `before-results` if it ran before the first outcome model (compare its date with the plan tag date); otherwise it is `after-results`.
| Q-ID | date | database | string | filters | hits | rows kept | consulted |
|---|---|---|---|---|---|---|---|
| Q<nn> | <YYYY-MM-DD> | <database or MCP tool> | <exact string as run> | <years, language, type \| none> | <n> | <n>: <R-ids> | <before-results \| after-results> |
| EXAMPLE Q01 | 2026-10-06 | OpenAlex | ("data exploration" OR "regression-type analyses") AND protocol AND ecolog* | 2000–2026; articles | 212 | 1: R01 | before-results |
| EXAMPLE Q02 | 2026-11-20 | Scopus | ("questionable research practices" OR HARKing) AND ecolog* | none | 47 | 1: R02 | after-results |

## (b) Reference rows
Stage 02 rows arrive from scan-notes.md as R rows with IDs unchanged (layer `scan`); stage 08 numbers on from the highest R.
| R-ID | DOI | source (first author, year, venue) | layer | resolver | resolve date | metadata match | retraction check | fulltext | sources path | risk | consulted | status |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| R<nn> | <10.xxxx/...> | <author, year, venue> | <scan \| global \| regional \| national \| local> | <crossref \| openalex \| pubmed \| mcp:<tool> \| user \| NA> | <YYYY-MM-DD \| NA> | <yes \| no: field(s) \| NA> | <clear \| RETRACTED \| not-run> <YYYY-MM-DD> | <yes \| no> | <sources/<file>.pdf \| URL \| none> | <high \| normal> | <before-results \| after-results> | <status> |
| EXAMPLE R01 | 10.1111/2041-210X.12577 | Zuur, 2016, Methods Ecol Evol | scan | crossref | <YYYY-MM-DD> | yes | clear <YYYY-MM-DD> | yes | sources/zuur2016.pdf | normal | before-results | `METADATA-OK` |
| EXAMPLE R02 | 10.1371/journal.pone.0200303 | Fraser, 2018, PLOS ONE | global | openalex | <YYYY-MM-DD> | yes | clear <YYYY-MM-DD> | no | none | normal | after-results | `METADATA-OK` (its CL rows cannot pass until the full text is read) |
| EXAMPLE R03 | <10.xxxx/...> | <author, year, regional venue> | regional | NA | NA | NA | not-run | yes | sources/<file>.pdf | high | after-results | `UNRESOLVED` |

## (c) Claim-support rows
| CL-ID | R-ID | claim (as worded in the draft) | verbatim quote | page or section | verifier | date | status |
|---|---|---|---|---|---|---|---|
| CL<nn> | R<nn> | <one sentence, no broader than the quote> | "<copied exactly from the full text>" | <p. n \| §n.n \| Table n> | <citation-verifier \| citation-verifier + human: initials \| NA> | <YYYY-MM-DD \| NA> | <status> |
| EXAMPLE CL01 | R01 | Data exploration (outliers, collinearity, dependence) should come before model fitting. | "<verbatim sentence from the R01 full text>" | <§n> | citation-verifier | <YYYY-MM-DD> | `SUPPORT-CHECKED` |
| EXAMPLE CL02 | R02 | About half of surveyed ecologists reported presenting an unexpected finding as if it had been hypothesised. | none (R02 has `fulltext: no`) | none | NA | NA | `UNRESOLVED` |

## Layer syntheses (stage 08; at most 15 lines per layer)
Built only from CL rows. Every sentence ends with `[ledger: <CL-ids>]`, and a sentence without one is deleted [D19, D21]. A synthesis is never cited itself: drafts cite the CL rows behind it.
### Global
- <one finding> [ledger: <CL-ids>]
### Regional
- <one finding> [ledger: <CL-ids>]
### National
- <one finding> [ledger: <CL-ids>]
### Local
- <one finding> [ledger: <CL-ids>]

## To-be-cited list (stage 08 writes it; stage 09 checks every row)
The stage 09 gate needs every CL row here at `SUPPORT-CHECKED` and its R row at `METADATA-OK`. Statuses live in tables (b) and (c) only.
| CL-ID | R-ID | draft section | human check |
|---|---|---|---|
| CL<nn> | R<nn> | <methods \| results \| intro \| discussion \| abstract> | <risk-high \| sample \| no> |
| EXAMPLE CL01 | R01 | methods | sample |
| EXAMPLE CL02 | R02 | intro | no (blocks the gate until CL02 is `SUPPORT-CHECKED`) |

## AI-summary provenance list (every row `NOT-CITABLE`)
These outputs are for orientation only, and no draft sentence may rest on them. A fact first found here can be cited only after it has its own R and CL rows [D19, D24, D25, D36].
| AI-ID | tool (name, version or model ID) | date | scope (sources loaded; question asked) | output kept at | used for | status |
|---|---|---|---|---|---|---|
| AI<nn> | <tool> | <YYYY-MM-DD> | <n sources, layer; prompt> | <path> | <which Q searches or outline it prompted> | `NOT-CITABLE` |
| EXAMPLE AI01 | NotebookLM | 2026-11-18 | 34 PDFs, regional layer; "What drives amphibian decline in <region> wetlands?" | ai01-notebooklm-regional.md | suggested search Q02 | `NOT-CITABLE` |
| EXAMPLE AI02 | Scopus AI (search assistant) | 2026-11-21 | answer to the Q02 query, 8 papers summarised | ai02-search-summary.md | which hits to screen first | `NOT-CITABLE` |

## Disclosure fields: fill at stage 10 (disclosure.md)
This is the checklist the main session completes in disclosure.md at stage 10; nothing is filled in here. Policy wording in our research comes from search snippets, so treat it as UNVERIFIED and re-read the live policy page [D27–D32].
- Target journal and AI policy: <journal> · <policy URL> · live page re-read on <YYYY-MM-DD>
- AI tools used: <name and model ID or version of each tool, including NotebookLM>
- Used for what: <data inventory | analysis code | literature extraction | citation checks | drafting | language editing>. Not used for: <research figures [D30] | scientific judgements, which stay with the authors>
- Human oversight: <who checked which outputs>. The authors take full responsibility [D26, D31].
- Where disclosed: <Methods | Acknowledgements | declaration section before References | cover letter>, as the target journal requires [D27, D28, D30, D32]
- Reference declaration, used only if every cited CL row is `SUPPORT-CHECKED` and every listed R row is `METADATA-OK`: "All references were checked to exist, to be cited accurately and to support the claims made." [D17]
