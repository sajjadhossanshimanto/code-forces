# https://codeforces.com/problemset/problem/1862/B

from collections import deque

for _ in range(int(input())):
    n = int(input())
    nums = deque(map(int, input().split()))
    
    l = [nums.popleft()]
    while nums:
        n = nums.popleft()
        if n<l[-1]:
            l.append(1)
        l.append(n)

    print(len(l))
    print(" ".join(map(str, l)))