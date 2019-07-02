y=int(input())
m=list(map(int,input().split()[:y]))
m.sort()
for i in  m:
    print(i,end=" ")
