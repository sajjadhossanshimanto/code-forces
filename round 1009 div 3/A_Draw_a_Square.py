def dis(x, y):
    return pow(x*x + y*y, .5)

for _ in range(int(input())):
    nx, px, ny, py = map(int, input().split())

    if dis(nx, ny)==dis(nx, py)==dis(px, ny)==dis(px, py):
        print("Yes")
    else:
        print("No")