from math_series import series


def test_assert_true():
    """ using this to check test working fine
    """
    assert True is True

""" test for the third figure in series 0,1,1"""
def test_fibonacci_at3():
    actual = 3
    expected = 1
    assert series.fibonacci(actual) == expected

"""" test for the first position when output should be 0"""
def test_fibonacci_at1():
    actual = 1
    expected = 0
    assert series.fibonacci(actual) == expected

""" test for answer at a large number"""
def test_fibonacci_at13():
    actual = 13
    expected = 144
    assert series.fibonacci(actual) == expected

""" test for lucas a a zero figure"""
def test_lucas_at0():
    actual = 0
    expected = "you'll need to enter a positive integer"
    assert series.lucas(actual) == expected

"""this tests lucas at a 1 which requires a special if figure"""
def test_lucas_at1():
    actual = 1
    expected = 2
    assert series.lucas(actual) == expected

""" this number tests the lucas number at the first sum figure"""
def test_lucas_at3():
    actual = 3
    expected = 3
    assert series.lucas(actual) == expected

""" This tests the lucas number at n=8"""
def test_lucas_at8():
    actual = 8
    expected = 29
    assert series.lucas(actual) == expected


