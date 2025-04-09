from calculator import add

def test_add_empty_string_returns_0():
    assert add("") == 0

def test_add_single_number_returns_itself():
    assert add("1") == 1

def test_add_two_numbers_comma_separated():
    assert add("4,5") == 9

test_add_empty_string_returns_0()
test_add_single_number_returns_itself()
test_add_two_numbers_comma_separated()
