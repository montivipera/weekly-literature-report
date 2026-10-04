# D. AI-assisted academic writing: citation fabrication, chained summaries, publisher policy, NotebookLM, good practice
Scope: evidence for a field ecologist drafting with Claude and summarising literature with NotebookLM; compiled 2026-10-04 (stream D of 5).
Method limit: every direct page fetch (Elsevier, Springer Nature, Wiley, T&F, ICMJE, COPE, Google help, PMC) was blocked by the network egress proxy, so policy and NotebookLM facts come from search-engine extracts and are flagged; study facts come from Consensus abstracts.
Grades: A peer-reviewed or official; B systematic independent / preprint audit; C anecdote, blog or third-party summary. UNVERIFIED = not confirmed against the primary page. 14 searches, 11 fetch attempts used (all blocked).

## Claims
| # | Claim | Source | Source date | Grade |
|---|---|---|---|---|
| 1 | GPT-3.5 fabricated 55% of citations, GPT-4 18%; 43% / 24% of the real ones had substantive errors | Walters & Wilder, Sci Rep, doi:10.1038/s41598-023-41032-5 | 2023 | A |
| 2 | Hallucination 39.6% (GPT-3.5), 28.6% (GPT-4), 91.4% (Bard) when replicating systematic-review reference lists; precision at most 13.4% | Chelli et al., JMIR, doi:10.2196/53164 | 2024-05 | A |
| 3 | GPT-3.5: 47% fabricated, 46% real but inaccurate, 7% fully accurate; wrong PMID in 93% of papers | Bhattacharyya et al., Cureus, doi:10.7759/cureus.39238 | 2023 | A |
| 4 | GPT-4o: 19.9% fabricated, 45.4% of real citations had errors (mostly invalid DOIs); fabrication 28-29% for low-visibility topics vs 6% for a well-known one; specialised prompts worse for one topic | Linardon et al., JMIR Ment Health, doi:10.2196/80371 | 2025-11 | A |
| 5 | Retrieval disabled, March 2026: 28.3% of 300 refs fabricated; GPT-5.3 27%, Grok-4 50%, DeepSeek-V3 8% | Seifi et al., Crit Care Explor, doi:10.1097/cce.0000000000001474 | 2026 | A |
| 6 | ChatGPT-5 (Dec 2025): 7.13% fabricated, only 49.3% bibliographically accurate; PMID wrong in 37% | Bernstein et al., Cureus, doi:10.7759/cureus.113654 | 2026 | A |
| 7 | Claude best of the general chatbots on spine-surgery citations (78.0% accurate); Gemini 26.2% fabricated; PubMed-indexed OpenEvidence 100%; patient-style prompts worse (n=10 questions per arm) | McLaughlin et al., Neurosurg Pract, doi:10.1227/neuprac.0000000000000244 | 2026 | A |
| 8 | Eight chatbots, 400 refs: 26.5% fully accurate; Copilot, Perplexity and Claude had the highest failure rates (free tiers) | Cabezas-Clavijo et al., J Data Inf Sci, doi:10.1515/jdis-2025-0326 | 2025 | A |
| 9 | Invalid-DOI rates checked against Crossref for GPT-4o-mini, Claude-3-haiku, Gemini-2.0-flash-lite, DeepSeek V3: >80% for lower-income-country topics, rising for 2020s publications | Kim et al., Publications, doi:10.3390/publications13040049 | 2025 | A |
| 10 | 10 LLMs, 69,557 citations checked via Crossref/OpenAlex/Semantic Scholar: 11.4-56.8% hallucinated; >3 LLMs citing the same work gives 95.6% accuracy | Naser, arXiv preprint, doi:10.48550/arxiv.2603.03299 | 2026 | B |
| 11 | 13 LLMs hallucinate 14.2-94.9% of citations; 1.07% of 56,381 AI/ML and security papers have invalid citations (+80.9% in 2025); 76.7% of surveyed reviewers do not check references | Xu et al. (GhostCite), arXiv, doi:10.48550/arxiv.2602.06718 | 2026 | B |
| 12 | Peer review does not reliably catch fabricated references: about 1 in 20 NeurIPS/USENIX 2025 papers has 2+ likely hallucinated refs; automated audit costs about $0.04 per paper | Russinovich et al. (RefChecker), arXiv, doi:10.48550/arxiv.2607.00738 | 2026 | B |
| 13 | Retrieval over 45M open-access papers gives citation accuracy on par with human experts; GPT-4o hallucinates citations 78-90% of the time in the same benchmark | Asai et al. (OpenScholar), Nature, doi:10.1038/s41586-025-10072-4 | 2026 | A |
| 14 | PubMed-API agent: 99.82% of citations real, but only 96.8% metadata-consistent with the in-text claim (Perplexity Sonar 89.1%) | Gorenshtein et al. (LITERAS), Comput Biol Med, doi:10.1016/j.compbiomed.2025.110363 | 2025 | A |
| 15 | RAG legal tools marketed as hallucination-free still hallucinate 17-33% | Magesh et al., arXiv, doi:10.48550/arxiv.2405.20362 | 2024 | B |
| 16 | Deep-research agents: link validity >94% and relevance >80% but factual support only 39-77%; accuracy falls as tool calls rise from 2 to 150 | Onweller et al., arXiv, doi:10.48550/arxiv.2605.06635 | 2026 | B |
| 17 | Web-grounded tools fabricate less but are fooled by Google Scholar [citation] stubs, retracted papers and refs that do not support the claim; Addiction now requires an author declaration that refs exist, are accurate and support claims | Brown et al., Addiction editorial, doi:10.1111/add.70379 | 2026 | A |
| 18 | Asking GPT-4 to verify and revise its own refs raised fully accurate refs from 7.5% to 77.5% (n=40, single model, authors graded) | Safran et al., Anatol Curr Med J, doi:10.38053/acmj.1746227 | 2025 | A |
| 19 | 4,900 LLM summaries (10 LLMs incl. Claude 3.7 Sonnet): most overgeneralised results even when told to be accurate; LLM summaries 4.85x more likely than human ones to overgeneralise; newer models worse | Peters et al., R Soc Open Sci, doi:10.1098/rsos.241776 | 2025 | A |
| 20 | Outside social sciences/humanities, main-result claims are stronger in abstracts and conclusions than in discussions, so abstract-only LLM answers risk overconfidence (single assessor model GPT-OSS 120B) | Thelwall, arXiv, doi:10.48550/arxiv.2605.27392 | 2026 | B |
| 21 | Recursive hierarchical merging of chunk summaries can amplify hallucination; re-injecting source context or citations to the input mitigates (legal and narrative texts, Llama 3.1) | Ou et al., arXiv, doi:10.48550/arxiv.2502.00977 | 2025 | B |
| 22 | Medical-evidence summaries: models struggle to identify salient information and are more error-prone over longer inputs | Tang et al., medRxiv, doi:10.1101/2023.04.22.23288967 | 2023 | B |
| 23 | Even when given the documents, open-weight models fabricate 1.2% at best (top-tier 5-7%) at 32K tokens, rising to >10% at 200K | Roig, arXiv, doi:10.48550/arxiv.2603.08274 | 2026 | B |
| 24 | NotebookLM: 13% of outputs had at least one hallucination vs 40% for ChatGPT/Gemini on a 300-document corpus; errors mostly unsupported characterisation of sources, not invented entities (journalism task) | Hagar et al., arXiv, doi:10.48550/arxiv.2509.25498 | 2025 | B |
| 25 | NotebookLM risk-of-bias scoring of 27 observational studies agreed poorly with manual scores (ICC 0.08-0.27; 14.8-29.6% agreement) | Beber et al., JPOSNA, doi:10.1016/j.jposna.2025.100294 | 2025 | A |
| 26 | Cochrane, Campbell, JBI and CEE position: authors stay responsible; AI use needs human oversight; any AI use that makes or suggests judgements must be fully reported; supports RAISE recommendations (sixth principle not captured) | Position statement, Environmental Evidence, https://pmc.ncbi.nlm.nih.gov/articles/PMC12594113/ (via search extract) | 2025-11 | A |
| 27 | Elsevier: declaration section before References naming tool, purpose and oversight; basic grammar/spelling checks exempt | Elsevier policy (via search extract), URL in matrix | undated | A |
| 28 | Springer Nature: LLMs fail authorship criteria; LLM use documented in Methods; AI-assisted copy editing exempt | Springer Nature policy (via search extract) | undated | A |
| 29 | Wiley: substantive AI editing, development or translation disclosed (Methods, disclosure or Acknowledgements); grammar tools exempt; authors verify claims and citations; reviewers may not upload manuscripts | Wiley AI guidelines (via third-party copies) | undated; a 2026 edition exists, date UNVERIFIED | A UNVERIFIED |
| 30 | T&F: disclose tool name, version, how and why in Methods or Acknowledgements; no generative AI for research figures; reviewers must not upload manuscripts or use AI to summarise them | T&F AI policy (via search extract) | undated | A |
| 31 | COPE: AI cannot be author; authors disclose tool and use in Materials and Methods (or similar) and remain fully responsible | COPE position (via search extract) | 2023 | A |
| 32 | ICMJE: disclose AI use at submission in cover letter and manuscript; writing help in Acknowledgements, analysis or figure use in Methods; AI cannot be author (Jan 2026 update exists, content not captured) | ICMJE (via Editage/CASRAI extracts) | 2023, upd. 2026 | A UNVERIFIED |
| 33 | NotebookLM answers carry inline citations linking to the relevant passages of your uploaded sources | Google blog (via search extract) | UNVERIFIED | A |
| 34 | NotebookLM limits by tier: 50 sources free, 100 Plus, 300 Pro, 600 Ultra; 500,000 words or 200 MB per source | University KB / third-party pages; older Google text says 25M words | 2025-26 | C UNVERIFIED |
| 35 | Google help pages are now titled "Gemini Notebook" (a summary says rename July 2026, notebooks kept) | support.google.com/notebooklm/answer/16454555 (title only) | 2026-07 | A, UNVERIFIED |
| 36 | No source found that NotebookLM citations carry PDF page numbers, or that page-numbered-quote prompts cut fabrication | none | n/a | UNVERIFIED |

## Citation fabrication: rates and controls
| Study | Model(s) | Fabrication / error rate | Control that helped |
|---|---|---|---|
| Walters 2023 | GPT-3.5, GPT-4 | 55% / 18% fabricated | newer model only |
| Chelli 2024 | GPT-3.5, GPT-4, Bard | 39.6 / 28.6 / 91.4% | none; manual validation advised |
| Bhattacharyya 2023 | GPT-3.5 | 47% fabricated, 93% wrong PMID | none |
| Linardon 2025 | GPT-4o | 19.9% fabricated; 45% of real had errors | none; niche topics worse |
| Seifi 2026 | GPT-5.3, Grok-4, DeepSeek-V3 | 27 / 50 / 8% fabricated | blinded check vs PubMed, DOI, Crossref |
| Cabezas-Clavijo 2025; McLaughlin 2026 | Claude among 8 chatbots; Claude vs others | Claude highest failure (free tier) vs 78% accurate (spine) | PubMed-indexed tool 100% |
| Kim 2025 | Claude-3-haiku and 3 others | DOI invalid >80% for some regions | Crossref API validation |
| Naser 2026 (preprint) | 10 LLMs | 11.4-56.8% | Crossref/OpenAlex/S2 lookup; >3-model consensus 95.6%; >2 repeats 88.9% |
| Asai 2026 (Nature) | OpenScholar vs GPT-4o | GPT-4o 78-90% hallucinated | retrieval plus self-feedback: human-level |
| Gorenshtein 2025 | LITERAS vs Sonar | 99.8% real; 96.8% metadata match | PubMed API agent loop |
| Magesh 2024 | Lexis+ AI, Westlaw AI | 17-33% | RAG reduces, does not eliminate |
| Onweller 2026 | 14 deep-research LLMs | 39-77% claim support | none; working links not enough |
| Safran 2025 | GPT-4 | 42.5% fabricated | self-verify prompt, n=40, weak design |

## Publisher policy matrix
Cells marked [mem] come from prior knowledge, not confirmed this session (UNVERIFIED). All four pages must be re-read before submission.
| Publisher | Allowed uses | Disclosure required where | Prohibited | Policy URL |
|---|---|---|---|---|
| Elsevier | Improving language and readability under human oversight [mem]; basic grammar checks need no declaration | Declaration section in the core manuscript before References: tool, purpose, oversight | AI as author [mem]; AI-generated or altered images outside method [mem]; reviewers uploading manuscripts [mem] | https://www.elsevier.com/about/policies-and-standards/the-use-of-generative-ai-and-ai-assisted-technologies-in-writing-for-elsevier |
| Springer Nature | AI-assisted copy editing (no declaration); other LLM use if documented | Methods section, or suitable alternative part | LLM as author; generative AI images [mem]; reviewers uploading manuscripts [mem] | https://www.springer.com/us/editorial-policies/artificial-intelligence--ai-/25428500 ; https://www.nature.com/nature-portfolio/editorial-policies/ai (not fetched) |
| Wiley | AI as companion to writing; grammar and spelling tools exempt | Methods, a disclosure statement or Acknowledgements | AI as author [mem]; replacing the author; reviewers uploading manuscripts (confirmed) | https://www.wiley.com/en-us/publish/article/ai-guidelines/ (canonical URL not confirmed; third-party copies only) |
| Taylor & Francis | Disclosed AI assistance; conceptual or flow-diagram illustrations if disclosed | Methods or Acknowledgements: tool, version, how, why | Generative AI for research images or figures; reviewers uploading manuscripts or summarising with AI; AI as author [mem] | https://taylorandfrancis.com/our-policies/ai-policy/ |
| COPE / ICMJE | Disclosed use; author fully accountable | COPE: Materials and Methods. ICMJE: cover letter plus Acknowledgements (writing) or Methods (analysis, figures) | AI as author | https://publicationethics.org/guidance/cope-position/authorship-and-ai-tools ; https://www.icmje.org/recommendations/browse/artificial-intelligence/ai-use-by-authors.html [mem] |

## NotebookLM: strengths / limits for literature work
- Grounded answers with inline citations that link to passages in your own sources (claim 33); a ready audit trail, but it checks only against what you uploaded.
- Independent tests: 13% of outputs hallucinated vs 40% for general chatbots (claim 24), yet poor agreement on structured appraisal (claim 25); neither used ecological literature.
- Typical failure is interpretive overconfidence: unsupported characterisation and attributed opinion turned into general statements (claim 24); matches LLM overgeneralisation (claim 19).
- Grounding is not immunity: given the documents, models still fabricate, and more so as context grows (claim 23); large notebooks raise that risk.
- No live DOI or Crossref check is documented; the notebook cannot tell if an uploaded PDF is a preprint, a retracted version or the wrong paper (inference, not sourced).
- Limits are tiered (claim 34) and Google help now says "Gemini Notebook" (claim 35); re-check limits and whether citations show page numbers in your own build (claim 36).
- Audio and Video Overviews are generated summaries of your sources; treat them as orientation aids, never as evidence to cite (inference).
- Sharing, data-use and training terms for uploaded manuscripts were not captured; confirm them before uploading unpublished drafts (see Gaps).

## Gaps
- No publisher, COPE, ICMJE or Google page could be fetched (egress proxy block), so wording and dates of policies are unverified; Elsevier, Springer Nature and Wiley prohibitions rely on prior knowledge.
- No peer-reviewed rate for current Claude models (Sonnet or Opus 4.x) with web search, citation tools or a Crossref check; Claude data are free-tier (2025), n=10 per arm (2026) or Claude-3-haiku.
- No direct test that page-numbered quotes or "quote verbatim" prompts lower fabrication; only indirect (claims 17, 21).
- No study of chained summaries (summary of a summary) on scientific claims; evidence is by analogy (claims 19-22). Abstract-vs-full-text evidence is one single-model preprint (claim 20).
- NotebookLM: PDF page numbers, current limits, sharing and training terms unverified; no ecology evaluation.
- RAISE recommendations themselves and the position statement's DOI and sixth principle were not read.
- Almost all fabrication data come from medicine or computer science; field ecology topics (niche, regional, post-2020) sit in the higher-risk regime (claims 4, 9).

## Implications for the workflow
- Citation ledger row per reference: DOI, resolver used (Crossref or OpenAlex), resolved title/first author/year/container versus what the draft says, match status, date checked, who checked. Existence checks are the proven control (claims 9, 10, 12); real refs still carry metadata errors in 24-45% of cases (claims 1, 4).
- Add a per-claim support record: claim sentence, source passage with page or section and verbatim quote, full text read yes/no (flag abstract-only), human verifier. A resolving DOI does not show the paper supports the claim (claims 14, 16, 17), and abstracts overstate (claim 20).
- Log provenance of every AI summary (tool, version, date, notebook or source set) and mark it "not citable"; cite the primary paper, and re-read it for any claim that will carry weight, since summaries overgeneralise (claims 19, 24).
- Keep disclosure fields in the ledger: tool name and version, purpose, extent of oversight, and the target journal's disclosure location (Elsevier pre-References; Springer Nature Methods; Wiley/T&F Methods or Acknowledgements; ICMJE cover letter plus section); also log "no unpublished manuscript uploaded to a training tool, no AI figures".
- Verify independently: the verifier is a database or a person, not the drafting model (claims 15, 18 show self- or RAG-checks miss errors); prioritise manual checks for post-2020, regional and niche-topic references (claims 4, 9).
