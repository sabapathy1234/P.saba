s1,a1=map(str,input().split())
for i in range(len(s1)):
    if(s1.count(s1[i])==a1.count(a1[i])):
        print("yes")
        break
    else:
        print("no")
        break
