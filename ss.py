n9 = int(input())
lst = [x9 for x9 in input().split()]
lst1 = []
for i9 in lst:
    if lst.count(i9) > 1:
        lst1.append(i9)
if len(lst1) == 0:
    print('unique')
else:
    print(' '.join(sorted(set(lst1))))
