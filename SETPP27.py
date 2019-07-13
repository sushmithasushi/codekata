s=input()
for i in s:
    if i.isupper():
        print(i.lower(),end="")    
    if i.islower():
        print(i.upper(),end="")
               
