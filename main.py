# SPDX-License-Identifier: MIT
"""Write the fridge-roast entry to the output directory."""
import os
from pathlib import Path

LINE = "My $3,000 smart fridge misreads expiry dates so confidently it binned today's yogurt, kept last month's fish, and emailed me a 12-page PDF defending the fish."


def main() -> None:
    # Gate guard: the roast must stay a single non-empty line of 1-200 chars.
    assert 1 <= len(LINE) <= 200 and "\n" not in LINE and LINE.strip()
    out_dir = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))
    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / "entry.txt").write_text(LINE, encoding="utf-8")


if __name__ == "__main__":
    main()
