nn=int(input())
l=list(map(int,input().split()[:nn]))
l.sort()
print(max(l))
