# https://codeforces.com/problemset/problem/1904/A

for _ in range(int(input())):
    a, b = map(int, input().split())
    kx, ky = map(int, input().split())
    qx, qy = map(int, input().split())

    move =  (
        (-a, b), (-a, -b),
        (a, b), (a, -b),
        (b, a), (b, -a),
        (-b, a), (-b, -a)
    )

    king = set()
    for cx, cy in move:
        king.add((kx + cx, ky + cy))
    
    queen = set()
    for cx, cy in move:
        queen.add((qx + cx, qy + cy))
    
    print(len(king & queen))