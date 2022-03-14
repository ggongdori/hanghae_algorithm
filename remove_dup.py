import sys
from itertools import combinations, permutations
from collections import deque

# ans = []
# s1_set = set(s2)
# s1_comb = permutations(s1_set, len(s1_set))
#
# for s in s1_comb:
#     ans.append(''.join(s))
#
# print(min(ans))

s1 = 'bcabc'
s2 = 'cbacdcbc'
# q = deque(s1[0])
ans = []

for i in range(len(s1)):
    if s1[i] in ans:
        continue
    #lexicographical order and the same char still in s1

    while ans and s1[i]<ans[-1] and ans[-1] in s1[i+1:]:
        ans.pop()
    ans.append(s1[i])
print(''.join(ans))



