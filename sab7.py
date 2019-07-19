sa1=int(input())
sa2=list(map(int,input().split()))
for sa in range(len(sa2)-1):
     if(sa2[sa]>sa2[sa+1]):
           print(sa)
           break
