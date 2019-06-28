e1,f1=map(int,input().split())
for g in range (e1+1,f1):
    z=0
    m=g
    while(m>0):
        a=m%10
        m=m//10
        b=a**3
        z=z+b
    if(g==z):
        print(z,end=' ')
