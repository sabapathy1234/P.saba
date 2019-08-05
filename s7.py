saba,imah=map(int,input().split())
list1=list(map(int,input().split()))
saba=[]
list1.insert(0,0)
for y in range(imah):
     vin=[]
     s=0
     bb,zz=map(int,input().split())
     for i in range(bb,zz+1):         
         s^=list1[i]     
     saba.append(s)
for y in saba:
     print(y)
