
def subarraySum(nums, k):
    bellow = [0]*(k+1)

    # 1. base case
    bellow[0] = 1

    # 2. loops
    for index in range(len(nums)-1, -1, -1):
        for left in range(k, nums[index]-1, -1):# k -> 1 
            not_pick = bellow[left]
            pick = bellow[left-nums[index]]
            "ensured in loop -> left will always greater or equal to nums[index]"
            
            bellow[left] = pick + not_pick
            # this pos -> represents value of the current pos
    return bellow[k]


inf = float("inf")
for _ in range(int(input())):
    n, k = map(int, input().split(" "))
    nums = list(map(int, input().split(" ")))

    pre = []
    min_value = [nums[0]]*n
    max_value = [nums[-1]]*n
    for i in range(1, len(nums)):
        min_value[i] = min(min_value[i-1], nums[i])
        max_value[n-i-1] = max(max_value[n-i], nums[n-i-1])
    
    # need to ans min max in range
    count = 0
    for i in range(n-1):
        print(min_value[i], max_value[i+1])
        if min_value[i]+max_value[i+1]==k:
            count+=1

    # print(count)
