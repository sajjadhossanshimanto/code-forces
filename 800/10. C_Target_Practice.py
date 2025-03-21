# https://codeforces.com/problemset/problem/1873/C



for _ in range(int(input())):
    row, column = 10, 10
    grid = []
    for _ in range(10):
        grid.append(input())
    
    score = 0
    for point in range(5):
        count = 0
        # for j in range(point, 10-point):
        count += grid[point][point:10-point].count("X")
        count += grid[10-point-1][point:10-point].count("X")

        for i in range(point+1, 10-point-1):
            if grid[i][point]=="X":
                count+=1
            if grid[i][10-point-1]=="X":
                count+=1

        score += count*(point+1)

        # print(count)
    print(score)