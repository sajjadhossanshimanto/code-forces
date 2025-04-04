# https://codeforces.com/problemset/problem/1726/A

#%% WA -> test cases are set to misunderstood
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    print(max(nums) - min(nums))

#%%