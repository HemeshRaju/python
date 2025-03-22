num=int(input("Enter the number:"))
a=0
b=1
for i in range(2,num):
    c=a+b
    a=b
    b=c
    print(c,end=" ")
print()