u12,v12=map(int,input().split())
l=list(map(int,input().split()[:u12]))
count=0
for i in l:
   if(i==v12):
      count=count+1
print(count)      
