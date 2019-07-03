zz=int(input())
x,y=0,1
print(y,end=" ")
res=0
for i in range(1,zz):
    res=x+y
    print(res,end=" ")
    x,y=y,res
    
    

