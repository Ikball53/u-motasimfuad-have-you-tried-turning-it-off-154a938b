"""One-line make.fun entry: a hopeless tech support agent's cheerful,
perfectly useless reassurance to a desperate customer."""

import os
from pathlib import Path

# The entry: the agent confesses his own gear fails just as often, then
# prescribes the classic reboot as if it were a solemn professional
# ritual — shared helplessness, delivered with a smile, fingers crossed.
LINE = "I totally understand — my own laptop froze three times today, so let's turn yours off, turn it on, and cross our fingers like professionals."

assert 1 <= len(LINE) <= 199, f"LINE must be 1-199 chars, got {len(LINE)}"


def main() -> None:
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_bytes(LINE.encode("utf-8"))


if __name__ == "__main__":
    main()
