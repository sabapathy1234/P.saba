#s
    
from itertools import permutations
n11, k11 = map(int, input().split())
x = list(map(int, input().split()))
for i in permutations(x, 2):
    if sum(i) == k11:
        print('yes')
        break
else:
    print('no')
