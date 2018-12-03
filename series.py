def fibonacci(n):
    """ This takes an 'n' from user and returns a number which is the nth position on Fibonacci sequence """
    subtotal1, subtotal2 = 0, 1
    if n < 0:
        return("you'll need to enter a positive integer")
    if n == 0:
        return (0)
    if n == 1:
        return (1)
    for i in range(2, n + 1):
        subtotal1, subtotal2 = subtotal2, subtotal1 + subtotal2
    return(subtotal2)


def lucas(n):
    """ This is a one argument function that returns a lucas number ()
    """
    subtotal1, subtotal2 = 2, 1
    if n < 0:
        return("you'll need to enter a positive integer")
    if n == 0:
        return (2)
    if n == 1:
        return (1)
    for i in range(2, n + 1):
        subtotal1, subtotal2 = subtotal2, subtotal1 + subtotal2
    return(subtotal2)


def sum_series(n, opt1=0, opt2=1):
    """This function uses optional inputs for the user to set up their own number sequences"""
    if n < 0:
        return("you'll need to enter a positive integer")
    if (opt1) < 0:
        return("you'll need to enter a positive integer")
    if opt2 < 0:
        return("you'll need to enter a positive integer")
    subtotal1, subtotal2 = opt1, opt2

    if n == 0:
        return opt1
    if n == 1:
        return opt2
    for i in range(2, n + 1):
        subtotal1, subtotal2 = subtotal2, subtotal1 + subtotal2
    return(subtotal2)


if __name__ == "__main__":
    print('fibonacci', fibonacci(3))
    print('lucas', lucas(3))
    print('sum', sum_series(3))
    print('sum', sum_series(3, 2, 1))
