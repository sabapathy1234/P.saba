y33,s33=list(map(int,input().split()))
y33s33=0
for i in range(y33,s33+1):
    if i>1:
        for x33 in range(2,i):
            if(i%x33==0):
                break
        else:
            y33s33+=1
print(y33s33)
