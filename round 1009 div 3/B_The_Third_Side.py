for _ in range(int(input())):
    n = int(input())
    nums = sum(map(int, input().split()))
    print(nums-n+1)