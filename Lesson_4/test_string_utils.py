import pytest
from string_utils import StringUtils

utils = StringUtils()


@pytest.mark.parametrize("input_str, expected", [
    ("skyeng", "Skyeng"),
    ("skyEng", "Skyeng"),
    ("", ""),
    ("   ", "   ")
])
def test_capitalize(input_str, expected):
    assert utils.capitilize(input_str) == expected


@pytest.mark.parametrize("input_str, expected", [
    ("    skyeng", "skyeng"),
    ("", ""),
    ("   ", "")
])
def test_trim(input_str, expected):
    assert utils.trim(input_str) == expected


@pytest.mark.parametrize("input_str, delimiter, expected", [
    ("s,k,y,e,n,g", ",", ["s", "k", "y", "e", "n", "g"]),
    ("1:2:3:4:5", ":", ["1", "2", "3", "4", "5"]),
    ("", "", []),
    (" , , ", ",", [" ", " ", " "])
])
def test_to_list(input_str, delimiter, expected):
    assert utils.to_list(input_str, delimiter) == expected


@pytest.mark.parametrize("input_str, char, expected", [
    ("skyeng", "s", True),
    ("skyeng", "a", False),
    ("", "s", False)
])
def test_contains(input_str, char, expected):
    assert utils.contains(input_str, char) is expected


@pytest.mark.parametrize("input_str, char, expected", [
    ("skyeng", "s", "kyeng"),
    ("skyeng", "sky", "eng"),
    ("", "s", ""),
    ("skyeng", "y", "skeng")
])
def test_delete_symbol(input_str, char, expected):
    assert utils.delete_symbol(input_str, char) == expected


@pytest.mark.parametrize("input_str, prefix, expected", [
    ("skyeng", "s", True),
    ("skyeng", "g", False)
])
def test_starts_with(input_str, prefix, expected):
    assert utils.starts_with(input_str, prefix) is expected


@pytest.mark.parametrize("input_str, suffix, expected", [
    ("skyeng", "g", True),
    ("skyeng", "k", False)
])
def test_end_with(input_str, suffix, expected):
    assert utils.end_with(input_str, suffix) is expected


@pytest.mark.parametrize("input_str, expected", [
    ("", True),
    ("   ", True),
    ("skyeng", False)
])
def test_is_empty(input_str, expected):
    assert utils.is_empty