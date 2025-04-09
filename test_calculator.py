from calculator import add

def test_add_empty_string_returns_0():
    assert add("") == 0

def test_add_single_number_returns_itself():
    assert add("1") == 1

test_add_empty_string_returns_0()
test_add_single_number_returns_itself()
