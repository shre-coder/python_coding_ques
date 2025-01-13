# Python Program to Check Leap Year
# year = 365days & leap year = 366days
# To be a leap year, the year number must be divisible by four – except for end-of-century years, which must be divisible by 400. This means that the year 2000 was a leap year, although 1900 was not. 2028, 2032 and 2036 are all leap years.

year = int(input("Enter the year: "))
if (year % 400 == 0) & (year % 100 == 0):
    print(year, "year is a leap year")
elif (year % 4 == 0) & (year % 100 != 0):
    print(year, "year is a leap year")
else:
    print(year, "year is a not a leap year")
