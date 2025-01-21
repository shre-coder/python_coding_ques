a = "Harry Potter and the goblet of Fire"

w = a.split()

# print(w)
for i in range(len(w)):
    w[i] = w[i].lower()

# print(w)

w.sort()
print(w)
