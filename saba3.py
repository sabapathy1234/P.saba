s1=input()
flag=1
vow=['a','e','i','o','u']
for v in vow:
    if(s1==v):
        print("Vowel")
        flag=0
        break
if(flag):
    if(s1>='a' and s1<='z'):
        print("Consonant")
    else:
        print("invalid")
