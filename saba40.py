ch22=input()
fi=0
for i in range(len(ch22)):
  if(ch22[i].isdigit() or ch22[i].isalpha() or ch22[i]==(" ")):
    continue
  else:
    fi+=1
print(fi)
  
