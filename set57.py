sss=int(input())
l=list(map(int,input().split()[:sss]))
s=0
for i in range(sss):
    s+=l[i]
print(s//sss)
