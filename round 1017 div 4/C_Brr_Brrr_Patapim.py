# https://codeforces.com/contest/2094/problem/C


for _ in range(int(input())):
    n = int(input())
    nums = []
    for i in range(n):
        nums.append(list(map(int, input().split())))
    
    p = [0] + nums[0]
    for i in range(1, n):
        p.append(nums[i][-1])
    
    p[0] = (1+2*n)*n - sum(p)# smart trick
    print(" ".join(map(str, p)))
