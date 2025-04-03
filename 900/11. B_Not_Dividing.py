# https://codeforces.com/problemset/problem/1794/B

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    if nums[0]==1:
        nums[0]+=1
    
    for i in range(1, n):
        if nums[i]==1:# NOTE: tricky edge cases
            nums[i]+=1

        if nums[i]%nums[i-1]==0:
            nums[i] += 1

    print(" ".join(map(str, nums)))
    