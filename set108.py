x=int(input())
xx=0
l=list(map(int,input().split()[:x]))
for i in range(len(l)-1):
    if (l[i]>l[i+1]):
        xx=i
print(l[xx-1])
