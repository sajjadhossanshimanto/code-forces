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

#%% ac without enen any further obtimisation
def rfind(arr, ele):
    for i in range(len(arr)-1, -1, -1):
        if arr[i]==ele:
            return i
    
    return -1

for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    min_left = [nums[0]]
    for i in range(1, n):
        min_left.append(min(nums[i],  min_left[-1]))
    # print(min_left)

    min_right = [nums[-1]]
    for i in range(n-2, -1, -1):
        min_right.insert(0, min(nums[i],  min_right[0]))
    # print(min_right)
    
    for i in range(1, n-1):
        if  nums[i] > min_right[i+1] and min_left[i-1] < nums[i]:
            print("YES")
            print(nums.index(min_left[i])+1, i+1, rfind(nums, min_right[i])+1)
            break
    else:
        print("NO")
