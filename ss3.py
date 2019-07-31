from itertools import combinations
N9,k9=map(int,input().split())
a=len(str(N9))
lst=list(combinations(str(N9),a-k9))
lst=sorted(lst)
print(*lst[0],sep='')
