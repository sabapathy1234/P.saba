ss1=int(input())
flag2=0
if(ss1>2):
    for i in range(2,int(ss1/2)+1):
        if ss1%i==0:
            print("yes")
            flag2=1
            break
if flag2==0 or ss1==2:
    print("no")
