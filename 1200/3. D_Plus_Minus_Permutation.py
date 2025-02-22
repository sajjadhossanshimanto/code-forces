# https://codeforces.com/problemset/problem/1872/D

for _ in range(int(input())):
    n, plus, minus = map(int, input().split())
    
    cummon = set(range(plus, n+1, plus)) & set(range(minus, n+1, minus))
    plus_num = n//plus-len(cummon)
    minus_num = n//minus-len(cummon)
    
    plus = set(range(n, n-plus_num, -1))
    minus = set(range(1, minus_num+1))
    
    print(sum(plus) - sum(minus))