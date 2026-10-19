"""Tiny text utility helpers used by the Dev Mode exit-gate demo."""


def normalize_spaces(text: str) -> str:
    """Collapse runs of whitespace to single spaces and strip the ends."""
    return " ".join(text.split())


def word_count(text: str) -> int:
    """Return the number of whitespace-separated words in ``text``."""
    return len(text.split())
