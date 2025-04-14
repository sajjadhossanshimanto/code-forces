# https://codeforces.com/contest/2094/problem/E
from itertools import zip_longest


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    set_bit = [0]*30  # Fix: size 30 for bits 0 to 29
    for i in nums:
        i = bin(i)
        for j in range(len(i)-1, 1, -1):
            if i[j]=="1":
                set_bit[len(i) - j-1] += 1
    
    # print(set_bit)
    ans = 0
    for k in nums:
        k = bin(k)
        total = 0
        for i in range(len(k)-1, 1, -1):
            pos_value = len(k) -i-1
            if k[i]=="0":
                total += (1<<pos_value)*set_bit[pos_value]
            else:
                total += (1<<pos_value)*(len(nums)-set_bit[pos_value])
        
        ans = max(total, ans)

    print(ans)
#%%
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    
    set_bit = [0] * 30
    for x in nums:
        for bit in range(30):
            if x & (1 << bit):
                set_bit[bit] += 1
    
    ans = 0
    for k in nums:
        total = 0
        for bit in range(30):
            if k & (1 << bit):
                total += (1 << bit) * (n - set_bit[bit])
            else:
                total += (1 << bit) * set_bit[bit]
        ans = max(ans, total)
    
    print(ans)