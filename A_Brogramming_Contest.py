for _ in range(int(input())):
    input()
    s = input()
    
    count = 0
    l = r =len(s)-1
    while l>=0:
        if s[l]=="1":
            while s[l]!="0" and l>=0:
                l-=1
            count+=1
            if s[r]=='0':
                count+=1
            r=l
            l-=1
        else:
            l-=1
    
    print(count)
