n = int(input("Enter a 3 digit number: "))

print("Prime factors:")

i = 2
while i <= n:
    if n % i == 0:
        print(i, end=" ")
        n = n // i
    else:
        i += 1