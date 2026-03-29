from __future__ import annotations

from pathlib import Path
from typing import Iterable

LOG_FILE = Path("log.txt")
DEFAULT_RATE = 1.15


def calculate_total(value: float, rate: float = DEFAULT_RATE) -> float:
    """Return the value after applying the configured multiplier rate."""
    return value * rate


def format_total_message(total: float) -> str:
    """Return a display string for a computed total."""
    return f"Total: {total:.2f}"


def append_totals_to_log(totals: list[float], log_file: Path = LOG_FILE) -> None:
    """Append the computed totals list to the log file.

    This is an explicit side-effect function separated from business logic.
    """
    with log_file.open("a", encoding="utf-8") as handle:
        handle.write(f"{totals}\n")


def process_data(data: Iterable[float], rate: float = DEFAULT_RATE, log_file: Path = LOG_FILE) -> list[float]:
    """Process input data by calculating totals, printing messages, and logging results."""
    totals = []

    for value in data:
        total = calculate_total(value, rate)
        message = format_total_message(total)
        print(message)
        totals.append(total)

    append_totals_to_log(totals, log_file)
    return totals
