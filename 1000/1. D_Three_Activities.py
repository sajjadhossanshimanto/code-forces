# https://codeforces.com/problemset/problem/1914/D

def find_pos(list_var, i, mx_idx):

    for j in range(3):
        if list_var[i]>maxes[mx_idx][0][j]:
            maxes[0][j] = (list_var[i], i)
            return
        
    # elif list_var[i]>maxes[mx_idx][1][0]:
    #     maxes[0][1] = (list_var[i], i)
    # elif list_var[i]>maxes[mx_idx][2][0]:
    #     maxes[0][2] = (list_var[i], i)

for _ in range(int(input())):
    n = int(input())
    sking = list(map(int, input().split()))
    movie = list(map(int, input().split()))
    games = list(map(int, input().split()))

    # i need to calculate 3 max values
    maxes = [[], [], []]
    '[skiing[(val, pos),], movie.., games..,]'
    for i in range(n):
        # sking
        if sking[i]>maxes[0][0][0]:
            maxes[0][0] = (sking[i], i)
        elif sking[i]>maxes[0][1][0]:
            maxes[0][1] = (sking[i], i)
        elif sking[i]>maxes[0][2][0]:
            maxes[0][2] = (sking[i], i)
        

        # for j in range(3):
            