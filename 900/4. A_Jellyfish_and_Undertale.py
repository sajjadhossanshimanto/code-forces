# https://codeforces.com/contest/1875/problem/A


for _ in range(int(input())):
    a, b, n = map(int, input().split())
    nums = list(map(int, input().split()))

    total = b
    for i in nums:
        total+=min(i, a-1)
    
    print(total)