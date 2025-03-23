from math import ceil, floor


for _ in range(int(input())):
    a, b, c = map(int, input().split())
    a+=ceil(c/2)
    b+=floor(c/2)

    if a>b:
        print("First")
    else:
        print("Second")