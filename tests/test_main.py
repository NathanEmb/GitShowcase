from showcase.main import greater_than_five


def test_greater_than_five():
    assert greater_than_five(5, inclusive=True)
    assert greater_than_five(6, inclusive=True)
    assert greater_than_five(6, inclusive=False)

    assert not greater_than_five(5, inclusive=False)
    assert not greater_than_five(4, inclusive=False)
    assert not greater_than_five(4, inclusive=True)

