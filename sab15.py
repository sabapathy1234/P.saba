s2,ss2=map(int,input().split())
intm=input().split()
a=[]
for i in intm:
  if (int(i)%2!=0):
    a.append(i)
print(a[ss2-1])
