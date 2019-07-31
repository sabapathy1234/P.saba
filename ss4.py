s,j1=input().split()
char=sj1s(len(j1)-len(s))
for g in range(len(s)):
  if(len(j)==1 and j1[g] in s):
    break
  if(s[g]!=j1[g]):
    char=char+1
print(char)
