n,mm=map(int,input().split())
m=mm
l=list(map(int,input().split()[:n]))
l.sort()
for i in l:
    if i<m:
        print(i,end=" ")
