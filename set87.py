ss=input()
l=len(ss)
x=l//2
ll=list(ss)
if x%2==0:
    ll[x]='*'
    ll[x+1]='*'
else:
    ll[x]='*'
for i in ll:
    print(i,end=" ")
    
