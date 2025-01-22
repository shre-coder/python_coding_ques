# Using Enumerate Method

# l = [34, 5, 61, 54, 89]
# for index, value in enumerate(l):
#     print(index, "-", value)

# Not using Enumerate Method

l = [34, 5, 61, 54, 89]
for index in range(len(l)):
    value = l[index]
    print(index, value)
