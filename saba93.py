s1=list(input())
b=[]
for i in s1:
    if i not in b:
        b.append(i)
if(s1==b):
    print("Yes")
else:
    print("No")
