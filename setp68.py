n=int(input())
l=list(map(int,input().split()[:n]))
c=1
res=1
m=1
for i in range(n-1):
    if l[i]==l[i+1]:
        c+=1
        res=c
    elif c>m:
        m=c
        res=c
        c=1
print(res)
