# for _ in range(int(input())):
#     n, k, x = map(int, input().split())
#     nums = list(map(int, input().split()))

#     l, r = 0, 1
#     window_sum = 0
#     count = 0
#     while r<=n:
#         while window_sum>x and l<r:
#             window_sum -= nums[l]
#             l+=1
        
#         while window_sum<x and r<n:
#             window_sum += nums[r]
#             r+=1
        
#         if window_sum==x:
#             count+=1
#             l+=1
#             window_sum -= nums[l-1]

#     print(count*k)


#%% grok gets tle at test case 4
def solve_test_case(n, k, x, a):
    # Since b repeats a k times, first create prefix sums for one cycle
    prefix = [0] * (n + 1)
    for i in range(n):
        prefix[i + 1] = prefix[i] + a[i]
    
    total_len = n * k  # length of array b
    cycle_sum = prefix[n]  # sum of one complete cycle
    
    # For each possible starting position l (1-based indexing)
    ans = 0
    for l in range(total_len):
        # Convert to 0-based indexing and find position within cycle
        l_pos = l % n
        # Number of complete cycles remaining after l
        cycles_left = (total_len - l - 1) // n
        # Maximum sum possible starting from l
        remaining_in_cycle = prefix[n] - prefix[l_pos]
        max_possible = remaining_in_cycle + cycles_left * cycle_sum
        
        if max_possible >= x:
            ans += 1
    
    return ans


t = int(input())
for _ in range(t):
    n, k, x = map(int, input().split())
    a = list(map(int, input().split()))
    print(solve_test_case(n, k, x, a))