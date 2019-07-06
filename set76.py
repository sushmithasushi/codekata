xx=int(input())
c=0
for i  in range(2,x):
    if xx%i==0:
        c+=1
if c==0:
    print("yes")
else:
    print("no")
