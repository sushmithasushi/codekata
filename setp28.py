x=int(input())
c=0
aa=[]
s=['a','a','b','i','k','l']
for i in range(x):
    aa.append(list(input()))
for i in range(len(aa)):
    if sorted(aa[i])==s:
        c+=1
print(c)
