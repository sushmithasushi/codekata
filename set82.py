s=input()
c=0
for i in s:
    if (i=='a' or i=='e' or i=='i' or i=='o' or i=='u'):
        c+=1
if c>=1:
    print("yes")
else:
    print("no")
        
