# num = int(input("Enter the number: "))
# fact = 1

# if num < 0:
#     print("factorial of 0 does not exist")
# if num == 0:
#     print("factorial of 0 is", 1)
# if num > 0:
#     for i in range(1, num + 1):
#         fact = fact * i
# print("The factorial of given nummber is ", fact)


# Using recursion
def fact(a):
    if a == 0:
        return 1
    else:
        return (a) * fact(a - 1)


num = int(input("enter a number here: "))

result = fact(num)
print("The factorial of the given number", result)
