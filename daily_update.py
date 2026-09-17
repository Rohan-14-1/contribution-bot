#!/usr/bin/env python3
"""
Daily Activity Logger
---------------------
Appends a timestamped log entry to `daily_activity.txt` each time it runs.
Works on macOS, Linux, and Windows using the Python standard library only.
"""

from datetime import datetime, timezone
from pathlib import Path


def log_daily_activity() -> None:
    # Resolve the repository root relative to this script location
    repo_dir = Path(__file__).resolve().parent
    activity_file = repo_dir / "daily_activity.txt"

    # Current UTC timestamp formatted as YYYY-MM-DD HH:MM:SS
    now_utc = datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
    entry = f"Daily activity: {now_utc}\n"

    # Append entry using UTF-8 encoding
    with open(activity_file, "a", encoding="utf-8") as f:
        f.write(entry)

    print(f"Recorded entry: {entry.strip()}")


if __name__ == "__main__":
    log_daily_activity()
