# https://codeforces.com/problemset/problem/1807/D

for _ in range(int(input())):
    n, q = map(int, input().split())
    nums = list(map(int, input().split()))

    pre_sum = [nums[0]]
    def range_sum(l, r):
        if l==0:# the only edge case in prefix sum
            return pre_sum[r]

        return pre_sum[r]-pre_sum[l-1]
    
    for i in range(1, n):
        pre_sum.append(pre_sum[-1]+nums[i])
    
    while q:
        l, r, k = map(int, input().split())
        l, r = l-1, r-1 # one indexed
        if ((r-l+1)*k + (pre_sum[-1] - range_sum(l, r)))&1:
            print("YES")
        else:
            print("NO")
        
        q-=1