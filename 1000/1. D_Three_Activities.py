# https://codeforces.com/problemset/problem/1914/D


def find_pos(list_var, i, mx_idx):

    for j in range(3):
        if list_var[i]>maxes[mx_idx][j][0]:
            maxes[mx_idx][j] = (list_var[i], i)
            return

for _ in range(int(input())):
    n = int(input())
    sking = list(map(int, input().split()))
    movie = list(map(int, input().split()))
    games = list(map(int, input().split()))

    # i need to calculate 3 max values
    maxes = [[(-1, -1), (-1, -1), (-1, -1)], [(-1, -1), (-1, -1), (-1, -1)], [(-1, -1), (-1, -1), (-1, -1)]]
    '[skiing[(val, pos),], movie.., games..,]'
    for i in range(n):
        # sking
        find_pos(sking, i, 0)
        find_pos(movie, i, 1)
        find_pos(games, i, 2)

    # do not over think. try all the possible value and take the. as there will be max 27 combinations
    ans = 0
    for i in maxes[0]:
        for j in maxes[1]:
            if i[1]==j[1]: continue
            for k in maxes[2]:
                if j[1]==k[1]: continue

                ans = max(i[0]+k[0]+j[0], ans)


    print(ans)