# https://codeforces.com/problemset/problem/1878/C

for _ in range(int(input())):
    n, k, x = map(int, input().split())
    max_sum = ((2*n-k+1)*k)/2
    min_sum = ((2+k-1)*k)/2
    if max_sum < x or x < min_sum:
        print("NO")
    else:
        # TODO: what are other cases that can hinder
        print("YES")