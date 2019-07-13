x=int(input())
ss=[str(i) for i in input().split(" ")]
ss.sort()
ss.sort(key=len)
print(ss,sep=" ")
