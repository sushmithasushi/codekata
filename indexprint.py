x=int(input())
l=list(map(int,input().split()[:x]))
for i in range(x):
    print(l[i] ,i)
