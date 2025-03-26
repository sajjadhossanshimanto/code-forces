# https://codeforces.com/problemset/problem/1806/A

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    # 2nd point must be positioed up
    if y2<y1:
        print(-1)
    elif x2-x1==y2-y1:# incase in same st-line
        print(y2-y1)
    else:
        x3 = y2-y1+x1
        if x2<=x3:
            print(y2-y1 + abs(x3-x2))
        else:
            print(-1)
