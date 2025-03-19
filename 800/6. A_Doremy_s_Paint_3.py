# https://codeforces.com/problemset/problem/1890/A

"got wa in test case 2"
for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    # if (2*sum(nums)-nums[0]-nums[-1])%(n-1)==0:
    #     print("Yes")
    # else:
    #     print("No")
    
    total = 2*sum(nums)
    for i in range(n):
        for j in range(i+1, n):
            if (total-nums[i]-nums[j])%(n-1)==0:
                print("Yes")
                break
        else:
            continue
        break
    else:
        print("No")
