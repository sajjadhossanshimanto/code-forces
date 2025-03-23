# https://codeforces.com/problemset/problem/1857/A

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