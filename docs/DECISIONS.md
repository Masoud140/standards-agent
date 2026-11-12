# Decisions (ADR numbering SA-nnn)

## SA-001 — Conventions shared with pdf2bim (2026-11-13, accepted)
- Docs in `docs/`: CURRENT_STATUS, NEXT_SESSION, DECISIONS, CHANGELOG, VERIFICATION_STRATEGY.
- Tests in `tests/`. Feature branches only; never push to `main`.
- pdf2bim ADR-005 (AI never approves) and ADR-009 (status discipline) apply verbatim.

## SA-002 — Licensed material stays out of git (2026-11-13, accepted)
- No standard PDFs, extracted text, table values or page images in the repository.
- Enforced by `.gitignore` and `tests/test_repo_hygiene.py`.
- Test fixtures use synthetic text only (invented clauses in an invented document).

## SA-003 — Index storage and encryption (open)
- To decide at the start of S1, after the licence check.
