x=int(input())
m=list(map(int,input().split()[:x]))
m.sort()
for i in  m:
    print(i,end=" ")
