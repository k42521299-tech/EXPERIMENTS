n = int(input("Enter a number: "))

t = n
s = 0
p = len(str(n))

while t > 0:
    d = t % 10
    s += d ** p
    t //= 10

if s == n:
    print("Armstrong number")
else:
    print("Not Armstrong number")