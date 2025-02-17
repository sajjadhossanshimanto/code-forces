s = list(input())

alp = "abcdefghijklmnopqrstuvwxyz"
for i in range(1, len(s)):
    if s[i]==s[i-1]:
        # change the char
        neiber = [s[i]]
        if i+1<len(s):
            neiber.append(s[i+1])
        
        for j in alp:
            if j not in neiber:
                s[i] = j
                break
    
print("".join(s))