# Python Program to Display Powers of 2 Using Anonymous Function.
# A power of 2 is the result of multiplying 2 by itself a certain number of times. For example, \(2^{2}=4\) and \(2^{3}=8\).
# An anonymous function is a function that is defined without a name. In Python, the lambda keyword is used to define anonymous functions.

nterms = int(input("Enter number of terms here: "))

result = list(map(lambda x: 2**x, range(nterms + 1)))

print(result)

for i in range(nterms + 1):
    print("the value of 2 raised to power", i, "is", result[i])
