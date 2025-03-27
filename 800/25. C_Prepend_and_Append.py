# https://codeforces.com/problemset/problem/1791/C

for _ in range(int(input())):
    n = int(input())
    s = (input())

    l, r = 0, n-1
    while s[l]!=s[r] and l<r:
        n-=2
        l+=1
        r-=1
    
    print(n)