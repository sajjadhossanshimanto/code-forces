n, k = map(int, input().split())
nums = list(map(int, input().split()))

div = n-(k-1)

total = 0
for i in range(k-1, len(nums)-k+1):
    total+=nums[i]
total = total*k/div
# print(total)

for i in range(k-1):
    #         (num * freq)  / div
    total += (nums[i]*(i+1))/div
    total += (nums[len(nums)-i-1]*(i+1))/div

print("{:.6f}".format(total))