# https://codeforces.com/contest/2072/problem/A

for _ in range(int(input())):
    a, k, p = map(int, input().split())

    k = abs(k)
    if a*p<k:
        print(-1)
        continue
    
    op = 0
    while k!=0:
        if k<p:
            p = k
        
        div, k = divmod(k, p)
        op += div

    if op>a:
        print(-1)
    else:
        print(op)
    