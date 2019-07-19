s1=input()
a1=len(v1)
b=[]
for x in range(0,l1,2):
    b.append(s1[x:x+2][::-1])
print(''.join(b))
