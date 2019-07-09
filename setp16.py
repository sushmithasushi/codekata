x,y=map(str,input().split())
if(len(x)!=len(y)):
    print("no")
else:
    c11=[x.count(i) for i in x]
    c22=[y.count(i) for i in y]
if(c11==c22):
    print("yes")
else:
    print("no")
