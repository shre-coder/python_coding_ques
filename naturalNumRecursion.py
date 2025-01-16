# Python Program to Find the Sum of Natural Numbers Using Recursion


def NaturalNumSum(n):
    if n <= 1:
        return n
    else:
        return n + NaturalNumSum(n - 1)


n = int(input("Enter a number here: "))
if n <= 0:
    print("Enter a positive number")
else:
    print("The sum of natural number upto ", n, "is ", NaturalNumSum(n))
