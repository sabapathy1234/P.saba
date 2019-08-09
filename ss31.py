#s    
w,s=list(map(int,input().split()))
ws=0
for i in range(w,s+1):
    if i>1:
        for x in range(2,i):
            if(i%x==0):
                break
        else:
            ws+=1
print(ws)
