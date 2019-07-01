x=int(input())
c=0
for i in range(2,x//2):
    if(x%i==0):
        c+=1
if c>0:
    print("no")
else:
    print("yes")
