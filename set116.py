c=0
x,yY=map(int,input().split())
l=list(map(int,input().split()[:x]))
for i in range(len(l)):
   if l[i]%2==1:
       c+=1
       if c==yY:
           print(l[i])
           break
