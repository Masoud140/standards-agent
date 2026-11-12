# Next session

1. Owner: complete `docs/LICENCE_CHECK.md` (text-and-data-mining terms). S0 closes on a "yes".
2. Owner: fill `docs/CORPUS_LIST.md` from the title page of each licensed copy
   (edition, amendment, holder of the licence). Do not fill from memory.
3. If the licence allows indexing: start S1 on a new branch `s1-wind-index`.
   - Decide index storage location and encryption (new ADR, SA-003).
   - Choose the PDF extractor; chunk by clause heading, tables and figures kept whole.
   - Chunk metadata: document, part, edition, amendment, clause id, title, page, superseded-by.
   - Scope: AS 5100.2 wind clause(s), AS/NZS 1170.2 (regions, terrain, shielding, drag figures),
     TfNSW wind requirements. Clause numbers are confirmed from the PDFs, not from the brief.
   - Done when: 20 chunks spot-checked against the PDF by the engineer.
4. If the licence does not allow indexing: stop and record the decision; consider a
   citation-only index (clause id, title, page; no text).
