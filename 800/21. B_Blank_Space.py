# https://codeforces.com/problemset/problem/1829/B

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    mx = 0
    ln = 0
    for i in nums:
        if i==0:
            ln+=1
            mx = max(mx, ln)
        else:
            ln = 0
    
    print(mx)