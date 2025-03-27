# https://codeforces.com/problemset/problem/1788/A

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    total = nums.count(2)
    if total&1:
        print(-1)
    else:
        count = 0
        for i in range(n):
            count += nums[i]==2
            if count==total//2:
                print(i+1) # 1 indexed based on the test results
                break

    # freq = [nums[0]==2]
    # for i in range(1, n):
    #     freq.append(nums[i]==2 + freq[i-1])
    
    # print(len(freq)==n)
