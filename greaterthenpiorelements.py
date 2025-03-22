a=[7,4,8,2,9]
max=a[0]
count=1
for i in range(1,len(a)):
    if a[i]>max:
        max=a[i]
        count+=1
print(count)