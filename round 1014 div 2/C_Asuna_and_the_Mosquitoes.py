# https://codeforces.com/contest/2092/problem/C


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    odd_sum = 0
    even_sum = 0
    for i in nums:
        if i&1:
            odd_sum+=i
        else:
            even_sum+=i
    
    if odd_sum&1==0:
        odd_sum-=1
    if odd_sum and even_sum:
        print(odd_sum+even_sum)
    else:
        print(max(nums))