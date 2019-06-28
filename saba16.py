lower,upper=map(int,input().split())
for num1 in range(lower,upper + 1):
    if num1 > 1:
        for i in range(2,num1):
            if (num1 % i) == 0:
                break
        else:
            print(num1,end=" ")
