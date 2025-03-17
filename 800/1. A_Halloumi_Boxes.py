def is_increasing(arr):
    if n==1: return True

    for i in range(1, n):
        if arr[i]<arr[i-1]:
            return False
    
    return True

for _ in range(int(input())):
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    if k>=2:
        print("YES")
    else:
        if is_increasing(arr):
            print("YES")
        else:
            print("NO")
