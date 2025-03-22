# https://codeforces.com/problemset/problem/1859/A

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()
    if nums[-1]==nums[0]:
        print(-1)
        continue

    # b = []
    # c = []
    # for i in nums:
    #     if i&1:
    #         b.append(i)
    #     else:
    #         c.append(i)
    
    # if not c:

    c=[nums.pop()]
    while nums[-1]==c[-1]:
        c.append(nums.pop())
    
    print(len(nums), len(c))
    print(" ".join(map(str, nums)))
    print(" ".join(map(str, c)))
    # print(" ".join(c))
