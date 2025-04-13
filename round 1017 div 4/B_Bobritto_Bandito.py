# https://codeforces.com/contest/2094/problem/B

for _ in range(int(input())):
    n, m, l, r = map(int, input().split())

    r1 = min(0+m, r)
    m = m-r1
    l1 = 0-m

    print(l1, r1)