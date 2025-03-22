a=[[2,1,1],[1,1,0],[0,1,1]]
count=0
for i in range(2):
    for j in range(2):
        if a[i][j]==2:
            a[i+1][j]=2
            a[i][j+1]=2
            a[i-1][j]=2
            a[i][j-1]=2
            count+=1
print(count)