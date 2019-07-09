x,y=map(int,input().split())
c=0
for i in range(x,y+1):
    if(i>1):
        for j in range(2,i):
            if i%j==0:
                break
        else:
            c+=1
print(c)
