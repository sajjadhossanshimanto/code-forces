def rfind(k, start=len(nums)-1, stop=-1):
    while start!=stop:
        if nums[start]==k:
            return start
        start-=1

def mx_value(freq:dict):
    mx = (-1, 0)
    for k, v in freq.items():
        if v>mx[1]:
            mx = (k, v)
    
    return mx

def shrink(start, stop, step=1):
    for i in range(start, stop, step):
        freq[nums[i]]-=1

for _ in range(int(input())):
    n, k = map(int, input().split())
    nums = list(map(int, input().split()))

    freq = {}
    mx = (-1, 0)
    for i in nums:
        freq[i] = freq.get(i, 0) + 1
        if freq[i] > mx[1]:
            mx = (i, freq[i])
    
    if k not in freq:
        print("NO")
    elif mx[0]==k:
        print("YES")
    
    l = nums.index(k)
    shrink(0, l)
    shrink(rfind(k), l, -1)
