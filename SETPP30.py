v11,v1,vz=list(map(str,input().split()))
vz=int(vz)
c1=0
for i in range(len(v11)):
  if(v11[i] != v1[i]):
    c1 += 1
if c1 == vz:
  print("yes")
else:
  print("no")
