x,y=map(int,input().split())
for i in range(x,y+1):
    s=0
    t=i
    j=i
    n=0
    while j>0:
        n=j%10
        s=s+n**3
        j=j//10
    if s==t:
        print(i)
    
