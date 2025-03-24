# https://codeforces.com/problemset/problem/1845/A

def target_sum(i, left_sum, path):
    if left_sum==0: return True, path[:]
    if i==len(nums): return False, []

    # pick
    if nums[i]<=left_sum:
        path.append(nums[i])
        r = target_sum(i, left_sum-nums[i], path)
        if r[0]:
            return r
        path.pop()
    
    # not-pick
    return target_sum(i+1, left_sum, path)


for _ in range(int(input())):
    target, k, x = map(int, input().split())
    nums = [i for i in range(k, 0, -1) if i!=x]
    # path = []
    r = target_sum(0, target, [])
    if r[0]:
        print("YES")
        print(len(r[1]))
        print(" ".join(map(str, r[1])))
    else:
        print("NO")