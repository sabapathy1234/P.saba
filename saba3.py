s=input()
flag=1
vow=['a','e','i','o','u']
for v in vow:
    if(s==v):
        print("Vowel")
        flag=0
        break
if(flag):
    if(s>='a' and s<='z'):
        print("Consonant")
    else:
        print("invalid")
