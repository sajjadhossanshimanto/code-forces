# https://codeforces.com/problemset/problem/1896/A

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    if sorted(nums)[0]==nums[0]:
        print("YES")
    else:
        print("NO")

        