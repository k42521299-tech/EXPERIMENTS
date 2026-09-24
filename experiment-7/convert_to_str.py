#WAP to convert a given list of integer and a tuple of integer in a list of string using map()
l = [1, 2, 3, 4, 5]
t = (6, 7, 8, 9, 10)

l = list(map(str, l))
t = list(map(str, t))

print("List of strings:", l)
print("Tuple of strings:", t)