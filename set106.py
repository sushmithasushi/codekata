x,y,z=map(int,input().split())
s=0
for i in range(z):
    s+=x
    x=x+y
print(s)
