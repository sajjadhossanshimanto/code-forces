# https://codeforces.com/problemset/problem/1831/A

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    middle_sum = n+1
    b=[]
    for i in nums:
        b.append(middle_sum-i)
    
    print(" ".join(map(str, b)))