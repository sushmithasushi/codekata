m,n=map(int,input().split())
l=list(map(int,input().split()[:m]))
for i in range(n):
    l.remove(l[-1])
for i in l:
    print(i,end=" ")
