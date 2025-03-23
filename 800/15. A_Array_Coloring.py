# https://codeforces.com/problemset/problem/1857/A
"""
In this problem, parity refers to whether a number (or sum of numbers) is even or odd.

- A number has even parity if it is divisible by 2 (e.g., 2, 4, 6, 8).
- A number has odd parity if it is not divisible by 2 (e.g., 1, 3, 5, 7).
"""


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    odd_counter = 0
    for i in nums:
        if i&1:
            odd_counter+=1
    
    # print(odd_counter)
    if odd_counter&1:
        print("NO")
    else:
        print("YES")