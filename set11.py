x,yy=map(int,input().split())
c=0
for i in range(min(x,yy),max(x,yy)+1):
    if i**2==x*yy:
        c=1
        break
if c==1:
    print("yes")
else:
    print("no")
