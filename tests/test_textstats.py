from textstats import normalize_spaces, word_count


def test_normalize_spaces_collapses_whitespace():
    assert normalize_spaces("  hello   world  ") == "hello world"


def test_word_count_counts_whitespace_separated_words():
    assert word_count("hello brave world") == 3


def test_word_count_collapses_runs_of_whitespace():
    assert word_count("  one\ttwo\n\nthree  ") == 3
