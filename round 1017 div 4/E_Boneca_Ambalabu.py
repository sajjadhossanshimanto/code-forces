from itertools import zip_longest


for _ in range(int(input())):
    n = int(input())
    nums = list(map(int, input().split()))

    # list(map(lambda x:x.count("1"), zip_longest(*map(lambda x: x[2:][::-1], map(bin, nums)), fillvalue="0")))
    set_bit = [0]*29
    for i in nums:
        i = bin(i)
        for j in range(len(i)-1, 1, -1):
            if i[j]=="1":
                set_bit[len(i) - j] += 1
    
    # print(set_bit)
    ans = 0
    for k in nums:
        k = bin(k)
        total = 0
        for i in range(len(k)-1, 1, -1):
            pos_value = len(k) -i
            if k[i]=="0":
                total += (1<<pos_value)*set_bit[pos_value]
            else:
                total += (1<<pos_value)*(len(nums)-set_bit[pos_value])
        
        ans = max(total, ans)

    print(ans)

