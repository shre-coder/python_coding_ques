# Using | operator

# dict1 = {"Shreyash": 89, "Nagesh": 99}
# dict2 = {"Nagesh": 95, "Ayushman": 78}

# print(dict1 | dict2)


# Using ** opeartor

# dict1 = {"Shreyash": 89, "Nagesh": 99}
# dict2 = {"Nagesh": 95, "Ayushman": 78}

# print({**dict1, **dict2})


# Using copy() and update() methods
dict1 = {"Shreyash": 89, "Nagesh": 99}
dict2 = {"Nagesh": 95, "Ayushman": 78}

dict3 = dict2.copy()
dict3.update(dict1)

print(dict3)
