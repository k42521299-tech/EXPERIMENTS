#ODD place in 5 digit number
x=int(input("enter a 5 digit number: "))
i=0
rev=0
while(x>0):
    dig=x%10
    rev=rev*10 + dig
    x=x//10
while rev>0:
    dig = rev%10
    i+=1
    rev=rev//10
    if(i%2!=0):
        print(dig)
