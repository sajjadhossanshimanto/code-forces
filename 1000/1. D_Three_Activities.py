# https://codeforces.com/problemset/problem/1914/D
from itertools import combinations_with_replacement


def find_pos(list_var, i, mx_idx):

    for j in range(3):
        if list_var[i]>maxes[mx_idx][j][0]:
            maxes[mx_idx][j] = (list_var[i], i)
            return

def find_bst_2(i, j):
    if i[1]==j[1]:
        if i[0]>j[0]:
            return True, False
        return False, True
    return True, True
    
def round_cycle(i):
    return (i+1)%3

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

    # ans = [0, 0, 0]
    # ans[0], ans[1] = find_bst_2(sking, movie)
    # find_bst_2(movie, games)

    # if maxes[0][0][1]!=maxes[1][0][1]!=maxes[2][0][1]:
    #     print()

    # i, j, k = 0, 0, 0
    # while ans[0]==ans[1] or ans[0]==ans[2] or ans[1]==ans[2]:
    # while i==j or i==k or j==k:
    #     if i==j:
    #         if sking[i]>movie[j]:
    #             j=round_cycle(j)
    #         else:
    #             i=round_cycle(i)
    #     elif i==k:
    #         if sking[i]>games[k]:
    #             k=j=round_cycle(k)
    #         else:
    #             i=round_cycle(i)
    #     elif j==k:
    #         if movie[j]>games[k]:
    #             k=j=round_cycle(k)
    #         else:
    #             j=round_cycle(j)

    # for i, j, k in combinations_with_replacement(range(3), 3):
    #     i, j, k = maxes[0][i], maxes[1][j], maxes[2][k]


    # do not over think. try all the possible value and take the 
    ans = 0
    for i in maxes[0]:
        for j in maxes[1]:
            if i[1]==j[1]: continue
            for k in maxes[2]:
                if j[1]==k[1]: continue

                ans = max(i[0]+k[0]+j[0], ans)


    print(ans)