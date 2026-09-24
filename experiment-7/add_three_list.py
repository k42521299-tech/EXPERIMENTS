#WAP to add three given lists of integers using python map() and lambda function
l1=[]
l2=[]
l3=[]
n=int(input("Enter the size of list:"))
for i in range(n):
    l1.append(int(input("Enter the number for list 1:")))
for i in range(n):
    l2.append(int(input("Enter the number for list 2:")))
for i in range(n):
    l3.append(int(input("Enter the number for list 3:")))

sum_list=list(map(lambda x,y,z: x+y+z,l1,l2,l3))
print("the sum of three arrays are:", sum_list)