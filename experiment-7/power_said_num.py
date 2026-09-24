# WAP to create a list containing the power of given number in bases raised to the corresponding number in the index

num = [2, 3, 4, 5, 6]

r = list(map(lambda x: x ** num.index(x), num))

print("Original List:", num)
print("Result:", r)