#WAP to convert all the characters into uppercase and lower case and eliminate duplicate letters from a given sequence. use map() function
s = input("Enter a sequence: ")

u = list(dict.fromkeys(s))

up = list(map(lambda x: x.upper(), u))

lo = list(map(lambda x: x.lower(), u))

print("After eliminating duplicates:", u)
print("Uppercase:", up)
print("Lowercase:", lo)