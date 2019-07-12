x=input()
y=''
Z='0ABCDEFGHIJKLMNOPQRSTUVWXYZABC'
for i in x:
    if i in Z:
        inpt4=Z.index(i)
        inpt4=inpt4+3
        y=y+Z[inpt4]
print(y)
