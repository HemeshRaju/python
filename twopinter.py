a=[1,0,2,3,2,0,0,4,5,1]
for x in a:
    if x==0:
        j=a.index(x)
        i=j+1
        if a[i]!=a[j]:
            a[i],a[j]=a[j],a[i]
        if a[i]==a[j]:
            i+=1
print(a)

