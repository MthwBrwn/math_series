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

"""tests code of series with only on input """
def test_sum_series_at_one_input():
    actual = 1
    expected = 0
    assert series.sum_series(actual) == expected


""" tests function when a single opt argument is made"""
def test_sum_series_at_two_inputs():
    actual = 4
    opt  = 1
    expected = 3
    assert series.sum_series(actual,opt) == expected

""" test if entering a zero produces same as default"""
def test_sum_series_at_two_inputs_zero_on_opt():
    actual = 4
    opt = 0
    expected = 2
    assert series.sum_series(actual) == expected

"""testing with zero in 2nd position"""
def test_sum_series_at_three_inputs_zero_on_opt2():
    actual = 4
    opt = 9
    opt2 = 0
    expected = 18
    assert series.sum_series(actual, opt, opt2) == expected








