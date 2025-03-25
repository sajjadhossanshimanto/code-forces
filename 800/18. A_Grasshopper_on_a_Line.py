# https://codeforces.com/problemset/problem/1837/A

for _ in range(int(input())):
    x, k = map(int, input().split())

    if x%k!=0:
        print(1)
        print(x)
    else:
        print(2)
        num = x-1
        while num%k==0 or (x-num)%k==0:
            num-=1
        print(num, x-num)