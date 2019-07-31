#s
p,s=map(int,input().split())
sp=list(map(int,input().split()))
l1=[]
for i in range(0,s):
     a,b=map(int,input().split())
     l1.append([a,b])
for i in range(s):
     lower=l1[i][0]
     upper=l1[i][1]
     x=sum(sp[lower-1:upper])
     print(x)
