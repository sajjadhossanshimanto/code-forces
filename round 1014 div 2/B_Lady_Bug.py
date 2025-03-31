# https://codeforces.com/contest/2092/problem/B

#%% WA
for _ in range(int(input())):
    n = int(input())
    a = input()
    b = input()
    
    a_odd_1 = 0
    a_even_1 = 0
    b_odd_0 = 0
    b_even_0 = 0
    for i in range(n):
        if i&1:
            a_odd_1 += 1 if a[i]=='1' else 0
            b_odd_0 += 1 if b[i]=='0' else 0
        else:
            a_even_1 += 1 if a[i]=='1' else 0
            b_even_0 += 1 if b[i]=='0' else 0

    if (a_odd_1 and a_odd_1>b_even_0) or (a_even_1 and a_even_1>b_odd_0):
        print("NO")
    else:
        print("YES")

