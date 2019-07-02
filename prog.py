n,a,d=map(int,input().split())
s=0
for i in range(1,n):
    t=(a+(n-1)*d)
    s+=t
print(s)
