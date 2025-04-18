# https://codeforces.com/problemset/problem/1726/A

#%% WA -> test cases are set to misunderstood
# for _ in range(int(input())):
#     n = int(input())
#     nums = list(map(int, input().split()))

#     print(max(nums) - min(nums))

#%%
# TODO: issu with multiple occurance
def arg_min_max(nums):
    mx, mn = max(nums), min(nums)
    max_list, min_list = [], []
    for i in range(len(nums)):        
        if nums[i] == mn:
            min_list.append(i)
        if nums[i] == mx:
            max_list.append(i)
    
    return min_list, max_list

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    min_list, max_list = arg_min_max(nums)
    for min_pos in min_list:
        for max_pos in max_list:
            if (max_pos==n-1 or min_pos==0) or (max_pos+1==min_pos):
                # if max min already in 0 or n or 
                # max is placed just in front of min
                print(nums[max_pos] - nums[min_pos])
                break
        else:
            continue
        break
    else:
        # need to sacrifise one
        if nums[0]-nums[min_pos] > nums[max_pos] - nums[n-1]:
            print(nums[n-1] - nums[min_pos])
        else:
            print(nums[max_pos] - nums[0])

#%% bluth-force -> 
# bluth force not always a bad thing actually
""" my problem was it is not alwasys the same that ans will come from max or min element 
any other adjoint may produce better results
"""
from itertools import islice


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    mx = 0
    # fix the 1st pos
    # mx = max(mx, max(islice(nums, 1, n)) - nums[0])
    # mx = max(mx, max(nums[1:]) - nums[0]) # ERROR: empty sequence in max function
    for i in range(1, n):
        mx = max(mx, nums[i] - nums[0])
    

    # fix the last pos
    # mx = max(mx, nums[-1] - min(islice(nums, n-1)))
    # mx = max(mx, nums[-1] - nums[:n-1]) # ERROR: empty sequence in max function
    for i in range(1, n):
        mx = max(mx, nums[n-1] - nums[i])

    # chose between any 2 adjoint
    for i in range(1, n):
        mx = max(mx, nums[i-1] - nums[i])

    print(mx)

