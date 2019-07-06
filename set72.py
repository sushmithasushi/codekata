s=input()
f=0
for i in s:
    if i=='1' or i=='0':
       f+=1
if f==len(s):
    print("yes")
else:
    print("no")
