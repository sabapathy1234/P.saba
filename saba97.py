s1=input()
p=[]
for i in s1:
    if(i.isnumeric()):
        p.append(i)
print(''.join(p))
