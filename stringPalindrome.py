a = input("Enter a word here: ")

rev = a[::-1]

if a == rev:
    print("It is a palindrome")
else:
    print("It is not a palindrome")
