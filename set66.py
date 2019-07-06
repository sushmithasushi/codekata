x=str(input())
l=len(x)
c=0
for i in x:
    if i.isalpha() or i.isnumeric():
        c+=1
if c==l:
    print("yes")
else:
    print("no")
