import math
c=0
xx,y=map(int,input().split())
for i in range(xx+1,y):
    s=math.sqrt(i)
    if (s-math.floor(s))==0:
            c+=1
print(c)
