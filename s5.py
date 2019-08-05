#s
s,j=map(int,input().split())
js=list(map(int,input().split()))
l1=[]
for i in range(0,j):
     a,b=map(int,input().split())
     l1.append([a,b])
for i in range(j):
     lower=l1[i][0]
     upper=l1[i][1]
     x=sum(js[lower-1:upper])
     print(x)
