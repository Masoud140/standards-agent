"""S0 guards: licensed material never enters git; the docs skeleton exists."""
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
BANNED_SUFFIXES = {".pdf", ".sqlite", ".faiss", ".parquet"}
BANNED_DIRS = {"index", "page_images", "extracted_text"}
REQUIRED_DOCS = [
    "CURRENT_STATUS.md", "NEXT_SESSION.md", "DECISIONS.md", "CHANGELOG.md",
    "VERIFICATION_STRATEGY.md", "LICENCE_CHECK.md", "CORPUS_LIST.md",
]


def tracked_files():
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True)
    return [Path(p) for p in out.stdout.splitlines() if p]


def test_no_licensed_file_types_tracked():
    bad = [p for p in tracked_files() if p.suffix.lower() in BANNED_SUFFIXES]
    assert not bad, f"licensed or index files tracked: {bad}"


def test_no_index_or_text_dirs_tracked():
    bad = [p for p in tracked_files() if p.parts and p.parts[0] in BANNED_DIRS]
    assert not bad, f"index or extracted text tracked: {bad}"


def test_corpus_folder_holds_only_readme():
    bad = [p for p in tracked_files() if p.parts[0] == "corpus" and p.name != "README.md"]
    assert not bad, f"files tracked under corpus/: {bad}"


def test_docs_skeleton_present():
    missing = [d for d in REQUIRED_DOCS if not (ROOT / "docs" / d).is_file()]
    assert not missing, f"missing docs: {missing}"


def test_gitignore_blocks_pdfs():
    assert "*.pdf" in (ROOT / ".gitignore").read_text().splitlines()
