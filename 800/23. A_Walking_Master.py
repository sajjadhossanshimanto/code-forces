# https://codeforces.com/problemset/problem/1806/A

for _ in range(int(input())):
    x1, y1, x2, y2 = map(int, input().split())

    # 2nd point must be positioed up
    if y2<y1:
        print(-1)
    elif x2-x1==y2-y1:# incase in same st-line
        print(y2-y1)
    elif x2<=x1:
        y3 = (x1+x2-y1-y2)/2# will definately be int
        x3 = (x1-x2-y1+y2)/2
        print(y3-y1 + y2-y3)
    else:
        print(-1)
