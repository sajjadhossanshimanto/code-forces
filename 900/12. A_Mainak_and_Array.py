# https://codeforces.com/problemset/problem/1726/A

#%% WA -> test cases are set to misunderstood
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    print(max(nums) - min(nums))

#%%
# TODO: issu with multiple occurance
def arg_min_max(nums):
    mx, mn = 0, 0
    for i in range(len(nums)):
        if nums[i] > nums[mx]:
            mx = i
        if nums[i] < nums[mn]:
            mn = i
    
    return mn, mx

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    min_pos, max_pos = arg_min_max(nums)
    if (max_pos==n-1 or min_pos==0) or (max_pos+1==min_pos):
        # if max min already in 0 or n or 
        # max is placed just in front of min
        print(nums[max_pos] - nums[min_pos])
    else:
        # need to sacrifise one
        if nums[0]-nums[min_pos] > nums[max_pos] - nums[n-1]:
            print(nums[n-1] - nums[min_pos])
        else:
            print(nums[max_pos] - nums[0])
    