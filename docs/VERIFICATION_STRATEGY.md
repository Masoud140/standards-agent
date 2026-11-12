# Verification strategy

| Check | Method | Phase |
|---|---|---|
| No licensed material in git | `tests/test_repo_hygiene.py` | S0 |
| Every chunk has document / edition / amendment / clause / page | automated on the index | S1 |
| Chunk text equals the PDF | engineer spot-check of 20 chunks | S1 |
| Applicability rules (wind region, importance, terrain, exposure) | unit tests on SB01, SB42, BR13A profiles | S2 |
| Clause recall | compare with a senior engineer's hand list (SB01, SB42); nothing missing | S3 |
| Zero uncited statements | automated: every clause claim carries document + page | S3 |
| Currency | every cited edition matches `CORPUS_LIST.md` | S3 |
| Register export loads | pdf2bim `Standards()` loads the file | S4 |

- Statuses: `placeholder-unverified` / `code-extracted-unverified` / `transcribed-unverified` /
  `checked` / `approved`. AI sets at most `transcribed-unverified`.
- The agent never states that a design complies.
