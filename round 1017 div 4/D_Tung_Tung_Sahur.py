# https://codeforces.com/contest/2094/problem/D

def same_char(l, s):
    r=l
    while r<len(s) and s[r]==s[l]:
        r+=1
    
    return l, r

for _ in range(int(input())):
    p = input()
    s = input()
    
    l, r = 0, 0
    l1, r1 = 0, 0
    flag = True
    while l<len(p) and l1<len(s):
        if p[l]!=s[l1]: # i was stupid to not chek this
            flag = False
            break

        l, r = same_char(l, p)
        l1, r1 = same_char(l1, s)

        if r1-l1>2*(r-l) or r1-l1<(r-l):
            flag = False
            break
        
        l = r
        l1 = r1
    if flag:# simple edge case 
        flag = l==len(p) and l1==len(s)
    
    if flag:
        print("YES")
    else:
        print("NO")

        

        

    