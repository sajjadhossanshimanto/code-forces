# https://codeforces.com/problemset/problem/1855/B

for _ in range(int(input())):
    n = int(input())

    i = 2
    while n%i==0:
        i+=1
    
    print(i-1)