xx=input()
l=len(xx)
f=0
for i in range(l):
    t=xx[i]
    for j in range(i+1,l):
        if xx[j]==xx[i]:
            f=1
            break
if f==1:
    print("no")
else:
    print("yes")
 
