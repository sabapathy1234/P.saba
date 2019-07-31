g9=int(input())
df9=[]
for i in range(0,g9):
 ij=input()
 df9.append(ij)
ff9=[]
for i in zip(*df9):
 if(i.count(i[0])==len(i)):
  ff9.append(i[0])
 else:
  break
print(''.join(ff9))
