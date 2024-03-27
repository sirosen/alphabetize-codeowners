from alphabetize_codeowners import sort_line


def test_case_insensitivity():
    assert sort_line("path @B @a @c") == "path @a @B @c"


def test_whitespace_normalization():
    assert sort_line(" path  @a  @b  @c ") == "path @a @b @c"
