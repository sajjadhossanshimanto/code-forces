# https://codeforces.com/contest/2093/problem/E
from itertools import islice


inf = float("inf")
for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    k = n//k

    min_mex = inf
    for i in range(0, n-k, k):
        sub = set(islice(nums, i, i+k))
        for i in range(n):
            if i not in sub:
                min_mex = min(min_mex, i)
                break
    
    print(min_mex)

        