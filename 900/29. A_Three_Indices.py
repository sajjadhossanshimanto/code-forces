# https://codeforces.com/problemset/problem/1380/A

#%% this might be fall
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    i = 1
    while i<n and nums[i-1]>=nums[i]:
        i+=1
    if n==i:
        print("NO")
        continue
    
    i, j = i-1, i
    while j<n-1 and nums[j]<=nums[j+1]:
        j+=1
    
    if j==n-1:
        print("NO")
        continue

    print("YES")
    print(i, j, j+1)
