x,k=map(int,input().split())
l=list(map(int,input().split()[:x]))
c=0
for i in l:
    if i==k:
        c+=1
if c==1:
    print("yes")
