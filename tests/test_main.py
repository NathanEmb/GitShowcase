from showcase.main import greater_than_five, string_reverser


def test_greater_than_five():
    assert greater_than_five(5, inclusive=True)
    assert greater_than_five(6, inclusive=True)
    assert greater_than_five(6, inclusive=False)

    assert not greater_than_five(5, inclusive=False)
    assert not greater_than_five(4, inclusive=False)
    assert not greater_than_five(4, inclusive=True)

def test_string_reverser():
    assert string_reverser('hello') == 'olleh'
    assert string_reverser('world') == 'dlrow'
    assert string_reverser("12345") == "54321"