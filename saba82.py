ss1=input()
n2=len(ss1)
if n2%2!=0:
    ss1=ss1[:int(n2/2)]+'*'+ss1[int(n2/2)+1:n2]
else:
    ss1=ss1[:int(n2/2)-1]+'**'+ss1[int(n2/2)+1:n2]
print(ss1)
