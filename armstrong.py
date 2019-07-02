x=int(input())
s=0
t=x
n=0
while x>0:
    n=x%10
    s=s+n**3
    x=x//10
if s==t:
    print("yes")
else:
    print("no")
