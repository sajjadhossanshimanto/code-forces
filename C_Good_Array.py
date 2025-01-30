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