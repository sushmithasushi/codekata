xx=input()
l=len(xx)
for i in range(l):
    if(i%2==0):
        print(xx[i],end="")
print(end=" ")
for i in range(l):
    if(i%2==1):
        print(xx[i],end="")
    
