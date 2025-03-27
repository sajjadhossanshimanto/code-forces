# https://codeforces.com/problemset/problem/1761/A

for _ in range(int(input())):
    n, p, q = map(int, input().split())
    
    if n==p==q:
        print("Yes")
    elif (p+q)<=(n-2):
        print("Yes")
    else:
        print("No")
