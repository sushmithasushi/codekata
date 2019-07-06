ss=input()
l=len(ss)
ll=list(ss)
x=l//2
if l%2==0:
    ll[x]='*'
    ll[x-1]='*'
else:
    ll[x]='*'
for i in ll:
    print(i,end=" ")
    

