n=int(input("Enter the number: "))
a=n
b=0
while a>0:
    r=a%10
    b=b*10+r
    a=a//10
if n==b:
    print("palindrome")
else:
    print("not palinrome")


