# https://codeforces.com/contest/2093/problem/C


def is_prime(num):
    if num==1: return False
    if num<=3: return True
    if num&1==0 or num%3==0: return False

    for i in range(5, int(pow(num, .5))+1, 6):
        if num%i==0 or num%(i+2): 
            return False
    
    return True

def solution(x, k):
    if k>1 and x>1: 
        # if k>1 not prime
        return False
    
    # now either k==1 or x==1
    if x==1:# edge case
        x = int("1"*k)
    
    return is_prime(x)



for _ in range(int(input())):
    x, k = map(int, input().split())
    
    print("YES" if solution(x, k) else "NO")