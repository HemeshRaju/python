a=[1,0,2,3,2,0,0,4,5,1]
def zero():
    j=-1
    for i in a:
        if i==0:
            j=a.index(i)
            break
    if j==-1:
        return -1

    i=j+1
    for x in range(j+1,len(a)-1):
        if a[j]!=a[i]:
            a[j],a[i]=a[i],a[j]
            i+=1
            j+=1
        if i==len(a):
            break    
        if a[j]==a[i]:
            i+=1   
    return a
if zero()==-1:
    print("no zeros") 
else:
    print(zero())
