# CLOSED-2026-10-19 — Kind-Overshoot not minted

**Timestamp:** 2026-10-19T17:47:25Z
**Session opened:** 2026-10-19T17:40:00Z (13:40 EDT)
**Session ID:** 2026-10-19-oa-pointer-without-bytes
**Author:** Haley Ann Bird
**Agent:** Grok by xAI. Does not own the work.
**Prior art checked:** Notion data source `collection://382d9c24-c10c-4fbf-9628-c7be3a1e4007` through CLOSED-2026-10-18b, and `sENZ5hFx/realm-discovery-engine-outputs` through 2026-10-18.
**IP readiness:** Logged. Not PPA Ready. A timestamp is not a filing.
**Score:** 0. **Novelty:** 0. **Coherence:** 0.92
**Status:** NOT_MINTED

## What was queued

Kind-Overshoot. Mint only when one pre-declared experiment, read from hashed PDF bytes, prints at least two pairs that close at the precision actually printed, and every closed row then lies on the opposite side of residual 1.7 from the shallow members, with no straddle and no subset promotion.

Used up, not re-scored: Doney et al. 2024 Table 5; Karakuş et al. 2025 Tables S2 and S3; Wang and Fennel 2024 (printed global fluxes 5.4 and 9.2 Pg C yr−1 at 100 m, no paired deep flux).

Next source, still unread as bytes: Walker and Palevsky 2025, doi:10.1029/2024GB008329, Table S2.

## What was retrieved

| Source | Claim | What the bytes were |
|---|---|---|
| Crossref | CC-BY version of record, license start 2025-04-19 | A license URL. Not a file. |
| Unpaywall | `is_oa` true, hybrid | `has_repository_copy` false. Best URL is Wiley `pdfdirect`. |
| OpenAlex | `is_oa` true, hybrid | `any_repository_has_fulltext` false. Same `pdfdirect` URL. |
| Semantic Scholar | `isOpenAccess` true, license CCBY | `openAccessPdf.url` is the DOI page, status HYBRID. Not a file. |
| Wayback CDX | query returned HTTP 200 | Body was `[]` for `agupubs.onlinelibrary.wiley.com/doi/*2024GB008329*`. No capture. |
| Wiley `pdfdirect` | the OA URL | HTTP 403, `text/html`, 5811 bytes, Cloudflare title "Just a moment...". SHA-256 `5ad2be59886e8a297bf288f1aab5b052de3aaf49caee4059e9feb786357d594d`. Does not start with `%PDF-`. |
| Wiley `/doi/pdf/` | same DOI | HTTP 403, HTML, 5793 bytes. SHA-256 `dc8b8567c888768e5b24a21b36cb69389f125b35fe779ba4f2ee1bc8d4eddb55`. |
| ESSOAR preprint doi:10.22541/essoar.172434585.50661378/v1 | preprint landing, not the version of record | HTTP 403, HTML, 5810 bytes. SHA-256 `85816770f9a5adfd80f3db46263344e61b747308c21ff390bd69c2d2c4af1e0d`. Not scored. Not a substitute table. |

No `CF-Ray` header was exposed by the client that hashed these bodies. Oct 18 recorded ray `a4c95d08bce3e99a-IAD` on a different fetch of the same URL class. The challenge HTML is not a stable document. These hashes identify today's error pages only.

Playwright is installed in the working environment and no Chromium binary is present, so a browser challenge was not executed. That is a tool gap, not a property of the paper.

## Screen

`oa_pointer_audit` on the records above → `OA_POINTER_WITHOUT_BYTES`, `mint_allowed_to_proceed` false.

`kind_overshoot` with `pdf_sha256` null → `PDF_BYTES_MISSING`, score 0.

A search-index excerpt of the Wiley HTML was quarantined by `quarantine_snippet` (`INDEX_EXTRACT_NOT_THE_FILE`). It is not a member list. It is not Table S2. The paper is not scored and not used up.

Historical control, not today's specimen: the Henson 2012 / DeVries & Weber 2017 / Nowicki 2022 pairs, forced through as if one source, still return `AXIS_DOES_NOT_CLOSE` (gaps 0.10, −0.151, −0.14). Treated honestly as three sources, the same function returns `GATE` because `one_source` is false. Neither result is minted. Both score 0. Doney, Karakuş, and Wang were not re-opened.

## Planes

No per-realm discovery was minted. One invention per realm stays refused.

| Plane | Result |
|---|---|
| Physical | No new force. 1.7 remains an inherited accounting magnitude. |
| Biological / deep ocean | The specimen was not read. No new flux. |
| Land | No kind axis in an unread table. No increment. |
| Animals | No increment. Fish rectangles stay with earlier classes. |
| Humans / neuroscience | No increment. Not promoted into a carbon rectangle. |
| Outer space | No increment. |
| Cross-realm | A leaderboard was not built. Darkness is not a score. |

## Leftover

**Kind-Overshoot remains queued.** A later session may mint it only when all of the following hold:

1. The PDF bytes of Walker and Palevsky 2025, or of Supporting Information S1 if that is where Table S2 lives, are hashed and start with `%PDF-`.
2. One pre-declared experiment in that file prints at least two pairs.
3. A row is closed when the product matches the deep flux at the precision actually printed.
4. Every closed row of that experiment is on the screen.
5. Shallow and deep lie on opposite sides of 1.7, with no straddle.
6. The shallow horizon is the horizon in that experiment's transfer definition.
7. A second experiment in the same source whose deep members cross 1.7 blocks promotion.

An OA flag, a CC-BY license, a DOI page, and a Cloudflare challenge page are not step 1.

## Do not re-issue

- Do not mint Kind-Overshoot from this session.
- Do not mark Walker and Palevsky 2025 used up.
- Do not score the search-index excerpt as Table S2.
- Do not re-score Doney Table 5, Karakuş S2/S3, or Wang and Fennel 2024.
- Do not mint 150 per-realm discoveries.
- Do not digitize an unread figure.
- Do not file this as a patent.

© 2026 Haley Ann Bird — original expression of this note only. The fluxes, if they are ever read, belong to Walker, Palevsky, and the other authors named above.
