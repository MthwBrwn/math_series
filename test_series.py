from math_series import series
# from math_series import fibonacci

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
def test_fibonacci_at0():
    actual = 1
    expected = 0
    assert series.fibonacci(actual) == expected

""" test for answer at a large number"""
def test_fibonacci_at13():
    actual = 13
    expected = 144
    assert series.fibonacci(actual) == expected

def test_fibonacci_as_string():
    actual = str
    expected = 144
    assert series.fibonacci(actual) == expected


