# https://codeforces.com/problemset/problem/1777/A

for _ in range(int(input())):
    n = int(input())
    nums = list(map(lambda x:int(x)&1, input().split()))

    if len(nums)==1:
        print(0)
    else:
        op = 0
        i = 1
        while i<len(nums):
            if nums[i]==nums[i-1]:
                op+=1
            i+=1
        print(op)


