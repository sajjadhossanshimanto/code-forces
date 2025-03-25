# https://codeforces.com/problemset/problem/1834/A
from math import ceil, floor


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    one_count = nums.count(1)
    minus_one_count = nums.count(-1)

    # both condition is meat
    if one_count>=minus_one_count and minus_one_count%2==0:
        print(0)
    # 1st condition is violated or both
    elif minus_one_count>one_count:
        op = ceil(n/2) - one_count
    
        op += 1 if floor(n/2)&1 else 0
        print(op)
    # only 2nd condition is violated
    elif minus_one_count&1:
        print(1)