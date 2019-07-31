a9,b9=input().split()
char=a9b9s(len(b9)-len(a9))
for g in range(len(a9)):
  if(len(b9)==1 and b9[g] in a9):
    break
  if(a9[g]!=b9[g]):
    char=char+1
print(char)
