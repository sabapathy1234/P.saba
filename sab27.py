string1 = input()
lengt1 = len(string1)
mylist = []
for i in range(0,lengt1,2):
    mylist.append(string1[i:i+2][::-1])
print("".join(mylist))
