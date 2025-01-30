#%% sol 1
n = int(input())
nums = list(map(int, input().split()))

ans = []
total = sum(nums)
for i in range(len(nums)):
    total -= nums[i]
    for j in range(len(nums)):
        if i==j: continue
        
        good_sum = total-nums[j]
        if good_sum==nums[j]:
            ans.append(i+1)
            break

    total += nums[i]

print(len(ans))
for i in ans:
    print(i, end=" ")
print()

#%% sol 2 different thinking
n = int(input())
nums = list(map(int, input().split()))

ans = []
total = sum(nums)
for i in range(n):
    for j in range(i+1, n):
        good_sum = total-(nums[i]+nums[j])
        if good_sum==nums[i]:
            ans.append(j+1)
        elif good_sum==nums[j]:
            ans.append(i+1)

print(len(ans))
for i in ans:
    print(i, end=" ")
print()
#%% actual solution
'''
we have to sum all numbers then
1. we must consider will there be any negative number
    - if not then the sumation will always be greater and greater
    - that means the sumation will be equal to the maximum number in the list 
    - unless we are seleting that maximum_num for removal. 
    - in that case the 2nd maxi will lead the sumation

2. after removal of a number num[i]=sum of rest
    - or we can say    num[i]+sum of rest => 2*num[i]


'''
# ai solution

n = int(input())
nums = list(map(int, input().split()))

total = sum(nums)  # Compute the sum of the entire array
max1, max2 = 0, 0  # Track the largest and second largest elements
max1_idx = -1      # Store the index of the largest element

# Find the two largest elements in one pass (O(n))
for i in range(n):
    if nums[i] > max1:
        max2 = max1
        max1 = nums[i]
        max1_idx = i
    elif nums[i] > max2:
        max2 = nums[i]

ans = []

# Check for "nice" indices in another pass (O(n))
for i in range(n):
    remaining_sum = total - nums[i]  # Sum after removing nums[i]

    # If nums[i] is the largest element, check if remaining sum is twice max2
    if nums[i] == max1:
        if remaining_sum == 2 * max2:
            ans.append(i + 1)  # Convert 0-based index to 1-based index
    else:
        if remaining_sum == 2 * max1:
            ans.append(i + 1)

# Output results
print(len(ans))
if ans:
    print(*ans)
