xx=int(input())
c=0
for i in range(2,xx+1):
    if xx%i==0:
        c+=1
if c>=1:
    print("yes")
else:
    print("no")
    
