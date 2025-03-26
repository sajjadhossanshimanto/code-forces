# https://codeforces.com/problemset/problem/1814/A

#%% try 1: tle
for _ in range(int(input())):
    n, k = map(int, input().split())

    if n&1==0:
        print("YES")
    elif n%k==0:
        print("YES")
    else:
        for i in range(n, -1, -k):
            if i&1==0:
                print("YES")
                break
        else:
            print("NO")

#%% ac
for _ in range(int(input())):
    n, k = map(int, input().split())

    if n&1==0:
        print("YES")
    # if odd -> k must be odd & k<=n
    elif k&1 and n>=k:
        print("YES")
    else:
        print("NO")