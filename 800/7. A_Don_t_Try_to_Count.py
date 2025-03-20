# https://codeforces.com/problemset/problem/1881/A

#%%
def is_sub_string(s1, ss, l=0):
    r =  l+len(ss)
    while r<=len(s1):
        for i in range(l, r):
            if s1[i] != ss[i-l]:
                break
        else:
            return True
        
        l+=1
        r+=1
    
    return False

# is_sub_string("abcdj", "asb")

#%%
for _ in range(int(input())):
    input()# n, m
    x = input()
    s = input()

    ans = 0
    if len(x)<len(s):
        # make x equvalent to s
        while len(x)<len(s):
            x+=x
            ans+=1
    
    if is_sub_string(x, s):
        print(ans)
    elif is_sub_string(x+x, s, len(x)-len(s)+1):
        print(ans+1)
    else:
        # print(ans+1)
        print(-1)



