# https://codeforces.com/problemset/problem/1900/A

for _ in range(int(input())):
    n = int(input())
    
    l = []
    mx = 0
    for i in input().split("#"):
        if not i: continue

        l.append(len(i))
        mx = max(mx, len(i))
    
    if mx>=3:
        print(2)
    else:
        print(sum(l))
