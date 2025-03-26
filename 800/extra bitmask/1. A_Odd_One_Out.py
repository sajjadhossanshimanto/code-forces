# https://codeforces.com/problemset/problem/1915/A


for _ in range(int(input())):
    nums = list(map(int, input().split()))
    res = 0
    for i in nums:
        res = res^i
    
    print(res)