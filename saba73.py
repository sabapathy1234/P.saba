S1=int(input())
flag2=0
if S1>2:
    for i in range(3,int(S1/2)):
        if S1%i==0:
            flag2=1
            print("no")
            break
if flag2==0 or S1==2:
    print("yes")
