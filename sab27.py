v1=input()
l1=len(v1)
z=[]
for x in range(0,l1,2):
    z.append(v1[x:x+2][::-1])
print(''.join(z))
