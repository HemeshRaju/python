list=[1,2,3,1,2]
len=len(list)
i=0
j=1
while i<=len:
    while j<=len-1:
        if (list[i]==list[j]):
            print(list[j])
            break
        j=j+1
    i=i+1

