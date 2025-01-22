marks = {"John": 23, "Lisa": 56, "Sid": 48}
print(marks)

# Sort the dictionary based on values
sv = sorted(marks.items(), key=lambda x: x[1])
print(sv)


# sort only the values
v = sorted(marks.values())
print(v)
