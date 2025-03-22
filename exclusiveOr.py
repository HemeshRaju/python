from functools import reduce
n=int(input("No of inputs:"))
x=int(input("Value of x:"))
a=input("input:").split(' ')
a=[int(i) for i in a]
subseq=[]
for i in range(len(a)):
    for j in range(i+1,len(a)+1):
        s=a[i:j]
        subseq.append(s)
print(subseq)
def exclusiveOr(list):
    return reduce(lambda x,y:x^y,list)
count=0
for i in subseq:
    if exclusiveOr(i)<x:
        count+=1
    print(exclusiveOr(i))
print("count:",count)