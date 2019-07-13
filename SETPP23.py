Xx,Yy=map(int,input().split())
x=list(map(int,input().split()[:Xx]))
y=list(map(int,input().split()[:Yy]))
for i in y:
    x.append(i)
print(max(x))
