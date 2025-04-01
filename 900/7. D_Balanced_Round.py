# https://codeforces.com/problemset/problem/1850/D
'the sample test cases were good wnough to understand the question'

for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))
    nums.sort()

    breaks = [0]
    for i in range(1, n):
        if nums[i] - nums[i-1] > k:
            breaks.append(i)
    breaks.append(n)

    to_keep = (0, 0)
    for i in range(1, len(breaks)):
        if breaks[i] - breaks[i-1] > to_keep[-1] - to_keep[0]:
            to_keep = (breaks[i-1], breaks[i])
    
    print(to_keep[0] + n-to_keep[-1])
