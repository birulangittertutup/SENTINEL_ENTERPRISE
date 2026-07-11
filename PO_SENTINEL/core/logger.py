from datetime import datetime
from pathlib import Path


LOG_DIR = Path("logs")
LOG_DIR.mkdir(exist_ok=True)


def write_log(message: str):

    log_file = LOG_DIR / f"{datetime.now():%Y-%m-%d}.log"

    with open(log_file, "a", encoding="utf-8") as f:
        f.write(
            f"[{datetime.now():%H:%M:%S}] {message}\n"
        )