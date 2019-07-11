x,yY=map(int,input().split())
l=list(map(int,input().split()[:x]))
l.sort()
print(l[yY-1])
