# Solution-1 : Using 3rd variable
# x = 13
# y = 10

# temp = x
# x = y
# y = temp
# print(x)
# print(y)

# Solution-2 : Without using 3rd variable
x = 12
y = 13

x, y = y, x
print("The value of x is: ", x)
print("The value of y is: ", y)
