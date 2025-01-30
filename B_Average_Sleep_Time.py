n, k = map(int, input().split())
nums = list(map(int, input().split()))

div = n-(k-1)

freq = min(n-k+1, k)
total = 0
for i in range(freq-1, len(nums)-freq+1):
    total+=nums[i]


for i in range(k-1):
    #         (num * freq)  / div
    total += (nums[i]*(i+1))/div
    total += (nums[len(nums)-i-1]*(i+1))/div

print("{:.6f}".format(total))


#%%
'''
10 7
8 16 2 13 15 9 5 13 9 2

ans: 68.25
out: 110.some
wrong ans because all nums are not at max frequency

'''

