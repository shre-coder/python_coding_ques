string = input("Enter something here: ")


try:
    num = int(input("enter a number here: "))
    print(string + num)
except (ValueError, TypeError) as a:
    print(a)

print("Thank you")
