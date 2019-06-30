x,y,z=map(int,input().split())
if x>y and x>z:
    print(x)
elif y>z and y>x:
    print(y)
else:
    print(z)
