x = int(input("Enter a number: "))

sum = 0

for i in range(1, x):
    if x % i == 0:
        sum += i

if sum == x:
    print("The number is perfect")
else:
    print("The number is not perfect")
