from collections import Counter


for _ in range(int(input())):
    n, k = map(int, input().split())
    s = input()
    freq = list(map(lambda x:x&1, Counter(s).values()))
    
    " thing is we have to have k elements removed"
    # try redusing the odd numbers to make them even
    odd_count = freq.count(1)
    if odd_count - k > 1 :
        print("NO")
    else:
        print("YES")
    '''
    if k < odd_counter:
        "we can't have more than 1 odd so"
        odd_counter - k <= 1 after substraction that must be less than or equal 1 for a yes
    if k > odd_counter:
        in case k is greater than odd_count then jackpot
        we have enough k to convert our all odd to even 

        after converting all odd to even no matter the leftover k is odd or even ans is yes
        if the leftover k is odd then in our palideom there will be one odd
    
    so in summery our ans is only no if odd_counter - k > 1
    '''
