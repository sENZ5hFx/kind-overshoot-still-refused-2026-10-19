"""Kind-Overshoot screen, 2026-10-19.

Official score stays 0 unless hashed PDF bytes contain a closed rectangle
that flips across the pre-declared residual. An open-access flag is not
those bytes. Not an ocean model. Not a carbon flux.
"""


def side(vals, residual):
    if not vals:
        return None
    if any(v == residual for v in vals):
        return 0
    if all(v < residual for v in vals):
        return -1
    if all(v > residual for v in vals):
        return 1
    return 0


def kind_overshoot(
    *,
    intact,
    stripped,
    products,
    residual,
    axis_published,
    one_source,
    same_units,
    support_kind,
    identity_abs_tol,
    pdf_sha256,
):
    """Screen one pre-declared experiment.

    intact: deep fluxes. stripped: shallow fluxes. products: shallow times
    the transfer printed in the same rows. pdf_sha256 must be 64 hex chars
    of a real PDF or the screen returns PDF_BYTES_MISSING and score 0.
    """
    out = {"score": 0.0, "novelty": 0.0, "verdict": None, "mint": False}
    if not pdf_sha256 or len(str(pdf_sha256)) != 64:
        out["verdict"] = "PDF_BYTES_MISSING"
        out["why"] = "No SHA-256 of PDF bytes. An OA flag cannot fill the table."
        return out
    if support_kind != "closed_pairs":
        out["verdict"] = "SUPPORT_NOT_CLOSED_PAIRS"
        return out
    if not (axis_published and one_source and same_units):
        out["verdict"] = "GATE"
        return out
    if min(len(intact), len(stripped), len(products)) < 2 or not (
        len(intact) == len(stripped) == len(products)
    ):
        out["verdict"] = "NOT_A_RECTANGLE"
        return out
    gaps = [round(p - i, 6) for p, i in zip(products, intact)]
    out["identity_gaps"] = gaps
    if any(abs(g) > identity_abs_tol for g in gaps):
        out["verdict"] = "AXIS_DOES_NOT_CLOSE"
        return out
    si, ss = side(intact, residual), side(stripped, residual)
    out["intact_side"], out["stripped_side"] = si, ss
    if si == 0 or ss == 0:
        out["verdict"] = "STRADDLE"
        return out
    if si == ss:
        out["verdict"] = "SAME_SIDE"
        return out
    out["verdict"] = "FLIP"
    out["score"] = 1.0
    return out


def oa_pointer_audit(records):
    """Separate an open-access pointer from a hashed PDF.

    records: non-empty list of dicts with source, http, starts_with_pdf,
    sha256, and optionally claims_oa and nbytes.
    Returns OA_POINTER_WITHOUT_BYTES when every OA claim fails to be a PDF.
    """
    if not isinstance(records, list) or not records:
        raise ValueError("records must be a non-empty list")
    pdfs = []
    pointers = []
    for r in records:
        for key in ("source", "http", "starts_with_pdf", "sha256"):
            if key not in r:
                raise ValueError("missing " + key)
        is_pdf = bool(r["starts_with_pdf"]) and r["http"] == 200 and r["sha256"]
        if is_pdf:
            pdfs.append(r["source"])
        elif r.get("claims_oa"):
            pointers.append(
                {
                    "source": r["source"],
                    "http": r["http"],
                    "sha256": r["sha256"],
                    "nbytes": r.get("nbytes"),
                }
            )
    if pdfs:
        return {
            "verdict": "PDF_PRESENT",
            "pdf_sources": pdfs,
            "mint_allowed_to_proceed": True,
        }
    return {
        "verdict": "OA_POINTER_WITHOUT_BYTES",
        "mint_allowed_to_proceed": False,
        "oa_pointers_that_are_not_pdfs": pointers,
        "why": "License and is_oa flags named a URL. The bytes are not a PDF.",
    }


def quarantine_snippet(snippet, pdf_sha256):
    """Refuse a number that was seen only in an index extract."""
    if pdf_sha256:
        return {"admitted": True, "reason": "backed by hashed PDF"}
    return {
        "admitted": False,
        "reason": "INDEX_EXTRACT_NOT_THE_FILE",
        "quarantined": snippet,
    }


if __name__ == "__main__":
    import json

    audit = oa_pointer_audit(
        [
            {
                "source": "wiley_pdfdirect",
                "claims_oa": True,
                "http": 403,
                "starts_with_pdf": False,
                "nbytes": 5811,
                "sha256": "5ad2be59886e8a297bf288f1aab5b052de3aaf49caee4059e9feb786357d594d",
            }
        ]
    )
    screen = kind_overshoot(
        intact=[],
        stripped=[],
        products=[],
        residual=1.7,
        axis_published=False,
        one_source=True,
        same_units=True,
        support_kind="closed_pairs",
        identity_abs_tol=0.02,
        pdf_sha256=None,
    )
    assert audit["verdict"] == "OA_POINTER_WITHOUT_BYTES"
    assert screen["verdict"] == "PDF_BYTES_MISSING" and screen["score"] == 0.0
    print(json.dumps({"audit": audit["verdict"], "screen": screen["verdict"], "score": 0}))
