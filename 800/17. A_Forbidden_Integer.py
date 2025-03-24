# https://codeforces.com/problemset/problem/1845/A

def target_sum(i, left_sum, path):
    if left_sum==0: return True, path[:]
    if i==len(nums): return False, []

    # pick
    if nums[i]<=left_sum:
        path.append(nums[i])
        r = target_sum(i, left_sum-nums[i], path)
        if r[0]:
            return r
        path.pop()
    
    # not-pick
    return target_sum(i+1, left_sum, path)


for _ in range(int(input())):
    target, k, x = map(int, input().split())
    nums = [i for i in range(k, 0, -1) if i!=x]
    
    dp = [[0]*(target+1) for _ in range(len(nums)+1)]
    
    # base case
    for i in range(len(nums)):
        dp[i][0] = 1
    
    # iterate
    for i in range(len(nums)-1, -1, -1):
        for left_sum in range(1, target+1):
            dp[i][left_sum] = dp[i][left_sum-nums[i]] or dp[i+1][left_sum]
    
    print(dp[0][target], target_sum(0, target, []))
    print(dp)

    # if r[0]:
    #     print("YES")
    #     print(len(r[1]))
    #     print(" ".join(map(str, r[1])))
    # else:
    #     print("NO")

for _ in range(int(input())):
    n, k, x = map(int, input().split())

    if x!=1:
        print("YES")
        print(n)
        print(" ".join(["1"]*n))
    else:
        if k==1:
            print("NO")
            continue

        # here k is at least 2
        if not n&1:
            print("YES")
            print(n//2)
            print(" ".join(["2"]*(n//2)))
            continue

        if k<3:
            print("NO")
            continue

        odd = n%2
        if odd==1:
            print("NO")
        else:
            print("YES")
            print(n//2+1)
            print(" ".join(["2"]*(n//2)), "3")