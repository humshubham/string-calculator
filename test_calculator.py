import pytest
from calculator import calc

def test_calc_empty_string_returns_0():
    assert calc("") == 0

def test_calc_single_number_returns_itself():
    assert calc("1") == 1

def test_calc_two_numbers_comma_separated():
    assert calc("4,5") == 9

def test_calc_multiple_comma_separated_numbers():
    assert calc("7,8,9,10") == 34

def test_calc_numbers_with_newline_delimiters():
    assert calc("11\n12,13") == 36

def test_calc_with_custom_delimiter():
    assert calc("//;\n1;2") == 3

def test_calc_with_negative_number_throws_exception():
    with pytest.raises(Exception) as e:
        calc("1,-2")
    assert "negative numbers not allowed -2" in str(e.value)

def test_calc_with_multiple_negatives_throws_exception():
    with pytest.raises(Exception) as e:
        calc("-1,-2,3")
    assert "negative numbers not allowed -1/-2" in str(e.value)

def test_calc_with_custom_delimiter_pipe():
    assert calc("//|\n1|2") == 3

def test_calc_with_custom_delimiter_star():
    assert calc("//*\n1*2") == 2