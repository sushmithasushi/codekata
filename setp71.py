nn=int(input())
l=list(map(int,input().split()[:nn]))
l.sort()
for i in range(0,len(l)-1):
    print(max(l[i],l[i+1]),end=" ")
