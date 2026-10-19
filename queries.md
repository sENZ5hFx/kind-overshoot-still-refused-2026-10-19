# Named queries — 2026-10-19

Prior-art scope before any candidate: Notion data source `collection://382d9c24-c10c-4fbf-9628-c7be3a1e4007`, rows through CLOSED-2026-10-18b, and `sENZ5hFx/realm-discovery-engine-outputs` through 2026-10-18. Kind-Overshoot was still queued. No 2026-10-19 repository existed at the start of the session.

## Retrieval attempts

1. Wiley `pdfdirect` and `/doi/pdf/` for doi:10.1029/2024GB008329 — HTTP 403, Cloudflare challenge HTML, hashed, not a PDF.
2. Unpaywall `10.1029/2024GB008329` — `is_oa` true, `has_repository_copy` false, best URL is the same `pdfdirect`.
3. OpenAlex work for the same DOI — `is_oa` true, `any_repository_has_fulltext` false, same URL.
4. Semantic Scholar graph API — `openAccessPdf.url` is the DOI page, status HYBRID, license CCBY.
5. Crossref — license CC-BY, content-version vor, start 2025-04-19. Link target is the Wiley PDF URL, intended application similarity-checking.
6. Wayback CDX for `agupubs.onlinelibrary.wiley.com/doi/*2024GB008329*` — HTTP 200, body `[]`.
7. ESSOAR preprint doi:10.22541/essoar.172434585.50661378/v1 — HTTP 403, challenge HTML, hashed. Not the version of record. Not scored.

## Not opened

- Walker and Palevsky 2025 PDF and Supporting Information. Still the queued source.
- Wang and Fennel 2024. Used up on 2026-10-18.
- Karakuş et al. 2025. Used up on 2026-10-16.
- Doney et al. 2024 Table 5. Used up on 2026-10-15.
- Friedlingstein Global Carbon Budget residual 1.7. Inherited, not re-measured.
