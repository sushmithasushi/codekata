n=int(input())
l=list(map(int,input().split()[:n]))
if n%2==1:
    s=n-1
else:
    s=n
for i in range(0,s,2):
    l[i],l[i+1]=l[i+1],l[i]
for i in l:
    print(i,end=" ")
