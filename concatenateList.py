# Using + operator
# l1 = [3, 6, 8, 2, "a", "j"]
# l2 = [3, 6, "k", "f", "j"]

# l12 = l1 + l2
# print(l12)

# with unique values
# l1 = [3, 6, 8, 2, "a", "j"]
# l2 = [3, 6, "k", "f", "j"]

# l12 = list(set(l1 + l2))
# print(l12)

# using extend() function
l1 = [3, 6, 8, 2, "a", "j"]
l2 = [3, 6, "k", "f", "j"]

l1.extend(l2)
print(l1)
