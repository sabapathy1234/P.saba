s1,ss1=list(map(int,input().split()))
sss1=list(map(int,input().split()))
ssss1=[]
for i in sss1:
    if i<=i+1:
        ssss1.append(i)
print(ssss1[ss1-1])
