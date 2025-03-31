# https://codeforces.com/contest/2092/problem/C
# sol: https://www.youtube.com/watch?v=9q6mHpEwYuY&t=920s

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    odd_count = 0
    even_counter = 0
    total = 0
    for i in nums:
        if i&1:
            odd_count += 1
        else:
            even_counter += 1
        
        total+=i
    
    if odd_count and even_counter:
        print(total-odd_count+1)
    else:
        print(max(nums))