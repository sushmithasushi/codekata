nn=int(input())
c=0
l=list(map(int,input().split()[:nn]))
for i in range(0,len(l)):
    for j in range(i+1,len(l)):
        if l[i]<l[j]:
            c+=1
print(c)
