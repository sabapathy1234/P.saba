a,b=map(int,input().split())
if(b<=100000):
    for x in range(a+1,b):
        if(x%2==0):
          print(x,end=" ")
