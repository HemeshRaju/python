a=[1,2,3,4,5,6,7,8,9,0]
l=a[0]
s=a[0]
secl=a[0]
secs=a[len(a)-1]
for i in a:
    if i>l:
        secl=l
        l=i
    if i<l:
        if i>secl:
            secl=i

for i in a:
    if i<s:
        secs=s
        s=i
    if i>s:
        if i<secs:
            secs=i

print(secl,secs)