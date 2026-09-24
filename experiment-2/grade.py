#Gradation system
a=int(input("enter the marks: "))
if(a>=0 and a<30):
    print("grade F")
elif(a>=30 and a<50):
    print("grade E")
elif(a>=50 and a<60):
    print("grade D")
elif(a>=60 and a<70):
    print("grade C")
elif(a>=70 and a<90):
    print("grade B")
elif(a>=90 and a<100):
    print("grade A")
else:
    print ("invaild marks")
