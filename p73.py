nn,n=map(int,input().split())
l=list(map(int,input().split()[:nn]))
a=l.index(n)
if abs(l[a]-l[a-1])==1 or abs(l[a]-l[a+1])==1:
  print(a+1)
