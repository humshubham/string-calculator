from calculator import add

def test_add_empty_string_returns_0():
    assert add("") == 0

def test_add_single_number_returns_itself():
    assert add("1") == 1

def test_add_two_numbers_comma_separated():
    assert add("4,5") == 9

def test_add_multiple_comma_separated_numbers():
    assert add("7,8,9,10") == 34

def test_add_numbers_with_newline_delimiters():
    assert add("11\n12,13") == 36

def test_add_with_custom_delimiter():
    assert add("//;\n1;2") == 3

test_add_empty_string_returns_0()
test_add_single_number_returns_itself()
test_add_two_numbers_comma_separated()
test_add_multiple_comma_separated_numbers()
test_add_numbers_with_newline_delimiters()
test_add_with_custom_delimiter()
