x,y=int(input().split())
x1,y1=int(input().split())
x2,y2=int(input().split())
m1=(y1-y)/(x1-x)
m2=(y2-y1)/(x2-x1)
if m1==m2:
    print("yes")
else:
    print("no")
