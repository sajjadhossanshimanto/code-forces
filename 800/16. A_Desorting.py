# https://codeforces.com/problemset/problem/1853/A
from math import ceil


def is_sorted(nums):
    for i in range(1, len(nums)):
        if nums[i] < nums[i-1]:
            return False
    
    return True

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    if not is_sorted(nums):
        print(0)
    else:
        min_diff = float("inf")
        for i in range(1, n):
            min_diff = min(min_diff, abs(nums[i] - nums[i-1]))
        
        # print(min_diff)
        print(max(1, (min_diff//2+1)))