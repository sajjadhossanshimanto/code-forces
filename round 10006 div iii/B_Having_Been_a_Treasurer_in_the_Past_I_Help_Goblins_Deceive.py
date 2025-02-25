# https://codeforces.com/contest/2072/problem/B

for _ in range(int(input())):
    n = int(input())
    s = input()

    dot = [0] * n
    dot[-1] = int(s[-1] == '-')
    dash = [0] * n
    dash[-1] = int(s[-1] == '_')
    for i in range(n-1, -1, -1):
        if s[i] == '-':
            dot[i] = dot[i+1] + 1
            dash[i] = dash[i+1]
        else:
            dot[i] = dot[i+1]
            dash[i] = dash[i+1] + 1
    
    # O(n^2) solution would get tle
    ans = 0
    for i in range(n):
        if s[i] == '-':
            for j in range(i+1, n):
                if s[j] == '_':
                    ans += dot[j]
                    
            ans += dash[i]



