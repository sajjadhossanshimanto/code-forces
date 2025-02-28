#%%
def is_fraction(n):
    return n-int(n)!=0

#%%
for _ in range(int(input())):
    k = int(input())
    n = (k-1)/3 + 1

    if not is_fraction(n):
        print("YES")
    else:
        print("NO")
