n=int(input())
a=input().split(' ')
a=[int(i) for i in a]
a.sort()
b=[]
print(a)
b.append(a[n-2])
b.append(a[1])
print(b)