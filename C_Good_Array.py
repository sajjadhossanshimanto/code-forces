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