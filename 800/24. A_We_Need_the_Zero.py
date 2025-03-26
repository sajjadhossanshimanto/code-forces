# https://codeforces.com/problemset/problem/1805/A

# WA code
for _ in range(int(input())):
    n = int(input())
    nums = list(filter(bool, map(int, input().split())))
    # print(len(nums))

    total = 0
    for i in nums:
        total ^= i
    
    if len(nums)%2==0:
        if total==0:
            print(0)
        else:
            print(-1)
    else:
        print(total)