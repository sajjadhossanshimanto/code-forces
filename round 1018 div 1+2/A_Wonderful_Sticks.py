# https://codeforces.com/contest/2096/problem/A
from collections import deque


for _ in range(int(input())):
    n = int(input())
    s = input()
    nums = deque(range(1, n+1))
    ans = deque()
    for i in range(len(s)-1, -1, -1):
        if s[i]=="<":
            ans.appendleft(nums.popleft())
        if s[i]==">":
            ans.appendleft(nums.pop())
    ans.appendleft(nums[0])

    print(" ".join(map(str, ans)))