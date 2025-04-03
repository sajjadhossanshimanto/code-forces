# https://codeforces.com/contest/2086/problem/C

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    que = list(map(int, input().split()))

    visit = set()
    ans = []
    zero_count = 0
    for i in que:
        i-=1
        while nums[i]!=0:

            nums[i], i = 0, nums[i]-1# converting to zero index
            # i = 
            zero_count += 1
        
        ans.append(zero_count)
    
    print(" ".join(map(str, ans)))