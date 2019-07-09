xx=list(input())
k=len(a)

for i in range(0,k,2):
    temp=xx[i]
    xx[i]=xx[i+1]
    xx[i+1]=temp
print("".join(xx))
    
