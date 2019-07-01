check3=int(input())
valid=list(map(int,input().split()[:check3]))
valid.sort()
for i in valid:
  print(i,end=" ")
