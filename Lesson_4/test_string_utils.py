from string_utils import StringUtils

utils = StringUtils()


def test_capitalize():
    assert utils.capitilize("skyeng") == "Skyeng"
    assert utils.capitilize("skyEng") == "Skyeng"
    assert utils.capitilize("") == ""
    assert utils.capitilize("   ") == "   "


def test_trim():
    assert utils.trim("    skyeng") == "skyeng"
    assert utils.trim("") == ""
    assert utils.trim("   ") == ""


def test_to_list():
    assert utils.to_list("s,k,y,e,n,g") == ["s", "k", "y", "e", "n", "g"]
    assert utils.to_list("1:2:3:4:5", ":") == ["1", "2", "3", "4", "5"]
    assert utils.to_list("") == []
    assert utils.to_list(" , , ") == [" ", " ", " "]


def test_contains():
    assert utils.contains("skyeng", "s") is True
    assert utils.contains("skyeng", "a") is False
    assert utils.contains("", "s") is False


def test_delete_symbol():
    assert utils.delete_symbol("skyeng", "s") == "kyeng"
    assert utils.delete_symbol("skyeng", "sky") == "eng"
    assert utils.delete_symbol("", "s") == ""
    assert utils.delete_symbol("skyeng", "y") == "skeng"


def test_starts_with():
    assert utils.starts_with("skyeng", "s") is True
    assert utils.starts_with("skyeng", "g") is False


def test_end_with():
    assert utils.end_with("skyeng", "g") is True
    assert utils.end_with("skyeng", "k") is False


def test_is_empty():
    assert utils.is_empty("") is True
    assert utils.is_empty("   ") is True
    assert utils.is_empty("skyeng") is False


def test_list_to_string():
    assert utils.list_to_string([1, 2, 3, 4, 5]) == "1, 2, 3, 4, 5"
    assert utils.list_to_string(["Sky", "eng"]) == "Sky, eng"
    assert utils.list_to_string([]) == ""
    assert utils.list_to_string([""]) == ""
