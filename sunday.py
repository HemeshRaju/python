a=input()
n=int(input())
week={'mon':6,'tue':5,'wed':4,'thu':3,'fri':2,'sat':1,'sun':0}
count=0
for i in week:
    if a==i:
        n=n-week[i]
        count+=1
def countsun(n):
    if n>=7:
        global count
        count=count+1
        n=n-7
        countsun(n)
    return count
print("number",countsun(n))
