# https://codeforces.com/problemset/problem/1380/A

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))
    nums.sort() # it haven't said that i can reorder

    i = 1
    while nums[i-1]==nums[i] and i<=n:
        i+=1
    if n==i:
        print("NO")
        continue
    
    i, j = i-1, i
    while nums[j]==nums[j+1] and j<n:
        j+=1
    
    if j==n-1 and nums[j]==nums[j-1]:
        print("NO")
        continue

    print("YES")
    print(i, j, j+1)



