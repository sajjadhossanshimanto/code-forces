# https://codeforces.com/problemset/problem/1766/A/

for _ in range(int(input())):
    n = int(input())

    if n<10:
        print(n)
        continue

    count = 0
    tester = 10
    while tester<n:
        count += 9
        tester*=10
    count+=n//(tester//10)
    print(count)