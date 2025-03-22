a=input().split(',')
def election():
    for i in range(len(a)-1):
        j=i-1
        k=i+1
        if a[i]=='A':
            if a[j]=='B':
                continue
            a[j]='A'
            j-=1
        if a[i]=="B":
            if a[k]=='A':
                continue
            a[k]='B'
            k+=1
    print(a)
    cada=a.count('A')
    cadb=a.count('B')
    if cada>cadb:
        print("A goverment")
    elif cadb>cada:
        print("B goverment")
    else:
        print("mix goverment")
election()