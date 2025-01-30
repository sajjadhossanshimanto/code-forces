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