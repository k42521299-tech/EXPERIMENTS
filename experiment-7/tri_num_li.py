#WAP to triple all numbers in a given list of integers. Use map() function
l1=[]
n=int(input("Enter the size of list:"))
for i in range(n):
    l1.append(int(input("Enter the number:")))
b= list(map(lambda x: x*3, l1))
print("The tripled numbers are:",b)