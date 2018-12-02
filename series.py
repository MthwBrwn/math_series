def fibonacci(n):
    """ """
    subtotal1, subtotal2 = 0, 1
    if n <= 0:
        return("you'll need to enter a positive integer")
    if n == 1:
        return (subtotal1)
    for i in range(n - 2):
        subtotal1, subtotal2 = subtotal2, subtotal1 + subtotal2
    return(subtotal2)


def lucas(n):
    """ This is a one argument function that returns a lucas number ()
    """
    subtotal1, subtotal2 = 2, 1
    if n <= 0:
        return("you'll need to enter a positive integer")
    if n == 1:
        return (subtotal1)
    for i in range(n - 2):
        subtotal1, subtotal2 = subtotal2, subtotal1 + subtotal2
    return(subtotal2)


def sum_series(n, opt1=0, opt2=1):
    """this function uses optional inputs for the user to set up their own number sequences"""
    if n <= 0:
        return("you'll need to enter a positive integer")
    if opt1 < 0:
        return("you'll need to enter a positive integer")
    if opt2 < 0:
        return("you'll need to enter a positive integer")
    subtotal1, subtotal2 = opt1, opt2
    if n == 1:
        return (subtotal1)

    for i in range(n - 2):
        subtotal1, subtotal2 = subtotal2, subtotal1 + subtotal2
    return(subtotal2)

# if __name__ == "__main__"
