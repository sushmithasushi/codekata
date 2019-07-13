x,yy=map(int,input().split())
while(yy>0):
  x,yy=yy,x%yy
  print(x)
