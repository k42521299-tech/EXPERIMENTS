#WAP to find the ratio of positive number, negative number and zeroes in an array of integer using map()
a = [1, -2, 0, 3, -4, 0, 5, -6]

p = list(map(lambda x: x > 0, a)).count(True)
n = list(map(lambda x: x < 0, a)).count(True)
z = list(map(lambda x: x == 0, a)).count(True)

print("Positive:", p)
print("Negative:", n)
print("Zero:", z)
print("Ratio:", p, ":", n, ":", z)