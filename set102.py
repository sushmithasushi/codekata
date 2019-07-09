x=int(input())
l=list(map(int,input().split()[:x]))
s=0
for i in range(len(l)):
     s+=l[i]
print(s)
