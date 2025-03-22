a=[1,1,2,2,3,3]
i=0
j=1
for x in range(len(a)-1):
    if i>=len(a)-1:
        break
    if j>=len(a)-1:
        break
    if a[i]==a[j]:
        i+=1
        j+=1
    if a[i]!=a[j]:
        j+=1
        a[i]=a[j]
print(a[:i+1])