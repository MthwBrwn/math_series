def fibonacci (n):
    subtotal1, subtotal2 = 0 , 1
    if n<= 0 :
        return("you'll need to enter a positive integer")
    if n == 1:
        return (subtotal1)
    for i in range(n - 2):
        subtotal1, subtotal2 = subtotal2, subtotal1 + subtotal2
    return(subtotal2)






# def lucas ():
#     pass

# if __name__ == "__main__"
