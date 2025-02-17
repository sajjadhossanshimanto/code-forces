n, k = map(int, input().split())
nums = list(map(int, input().split()))

pre_sum = [0]*n
pre_sum[0] = nums[0]
for i in range(1, n):
    pre_sum[i]=pre_sum[i-1] + nums[i]
# print(pre_sum)

def range_sum(l, r):
    return pre_sum[r] - (pre_sum[l-1] if l > 0 else 0)

total = 0
# k-=1
for i in range(k-1, n):
    total += range_sum(i-k+1, i)
    # print((i-k+1, i))

# print(total)
print(total/(n-k+1))

#%%
'''
10 7
8 16 2 13 15 9 5 13 9 2

ans: 68.25
out: 110.some
wrong ans because all nums are not at max frequency

'''

