saba10,pathi10=map(int,input().split())
maxima=max(saba10,pathi10)
while(1):
 if(maxima%saba10==0 and maxima%pathi10==0):
  print(maxima)
  break
 maxima+=1
