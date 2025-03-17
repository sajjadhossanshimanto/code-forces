for _ in range(int(input())):
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))

    volume = arr[0]
    for i in range(1, n):
        volume = max(volume, abs(arr[i]-arr[i-1]))
    
    volume = max(volume, 2*abs(arr[-1]-x))
    print(volume)
