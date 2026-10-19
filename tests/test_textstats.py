from textstats import normalize_spaces


def test_normalize_spaces_collapses_whitespace():
    assert normalize_spaces("  hello   world  ") == "hello world"
