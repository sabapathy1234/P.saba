source6=int(input())
final=list(map(int,input().split()[:source6]))
final.sort()
for i in final:
  print(i,end=" ")
