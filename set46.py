sa=input()
c=0
for i in sa:
    if(i.isdigit() or i.isalpha() or i==(" ")):
        continue
    else:
        c+=1
print(c)
