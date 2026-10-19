"""Tiny text utility helpers used by the Dev Mode exit-gate demo."""


def normalize_spaces(text: str) -> str:
    """Collapse runs of whitespace to single spaces and strip the ends."""
    return " ".join(text.split())
