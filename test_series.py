from math_series import series


def test_assert_true():
    """ using this to check test working fine
    """
    assert True is True


def test_fibonacci_at3():
    """ test for the third figure in series 0,1,1,2,"""
    actual = 3
    expected = 2
    assert series.fibonacci(actual) == expected


def test_fibonacci_at1():
    """ testing at position 1"""
    actual = 1
    expected = 1
    assert series.fibonacci(actual) == expected


def test_fibonacci_at7():
    """ test for answer at a large number"""
    actual = 7
    expected = 13
    assert series.fibonacci(actual) == expected


def test_lucas_at0():
    """ test for lucas a a zero figure"""
    actual = 0
    expected = 2
    assert series.lucas(actual) == expected


def test_lucas_at1():
    """this tests lucas at a 1 """
    actual = 1
    expected = 1
    assert series.lucas(actual) == expected


def test_lucas_at3():
    """ this number tests the lucas number at the first sum figure"""
    actual = 3
    expected = 4
    assert series.lucas(actual) == expected


def test_lucas_at8():
    """ This tests the lucas number at n=8"""
    actual = 8
    expected = 47
    assert series.lucas(actual) == expected


def test_sum_series_at_one_input():
    """tests code of series with only on input """
    actual = 1
    expected = 1
    assert series.sum_series(actual) == expected


def test_sum_series_at_two_inputs():
    """ tests function when a single opt argument is made"""
    actual = 4
    opt = 1
    expected = 5
    assert series.sum_series(actual, opt) == expected


def test_sum_series_at_two_inputs_zero_on_opt():
    """ test if entering a zero produces same as default"""
    actual = 4
    expected = 3
    assert series.sum_series(actual) == expected


def test_sum_series_at_three_inputs_zero_on_opt2():
    """testing with zero in 2nd position"""
    actual = 4
    opt = 9
    opt2 = 0
    expected = 18
    assert series.sum_series(actual, opt, opt2) == expected


def test_sum_series_with_neg_number():
    """testing with a neg n """
    actual = -2
    expected = "you'll need to enter a positive integer"
    assert series.sum_series(actual) == expected








