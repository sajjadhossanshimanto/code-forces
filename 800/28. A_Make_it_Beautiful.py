# https://codeforces.com/problemset/problem/1783/A

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort()

    # ln = 2
    if nums[0]==nums[-1]:
        print("NO")
        continue

    pre_sum = nums[0]+nums[-1]
    l, r = 1, n-2
    while l<r:
        if pre_sum==nums[l]:
            print("NO")
            break
        l+=1
        r-=1
    else:
        print("YES")
        for i in range(n//2):
            print(nums[i], nums[n-i-1], end=" ")
        
        if n&1:
            print(nums[n//2])
        else:
            print()

