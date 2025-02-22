# https://codeforces.com/problemset/problem/1872/D

#%% 1st approach
for _ in range(int(input())):
    n, plus, minus = map(int, input().split())
    
    cummon = set(range(plus, n+1, plus)) & set(range(minus, n+1, minus))
    plus_num = n//plus-len(cummon)
    minus_num = n//minus-len(cummon)
    
    plus = set(range(n, n-plus_num, -1))
    minus = set(range(1, minus_num+1))
    
    print(sum(plus) - sum(minus))

''' gets tle
test case: t-> 10^4 O(10^4)
n -> 10^9 range funtion takes O(n)
set operation takes O(n)
sum takes O(n)
total O(n^2*t) -> 10^17
'''
#%% 2nd approach
def range_sum(l, r):
    ''' sum of numbers from l to r 
    formula: (first + last) * n//2
    '''
    return (l+r)*(r-l+1)//2

for _ in range(int(input())):
    n, plus, minus = map(int, input().split())
    
    cummon = set(range(plus, n+1, plus)) & set(range(minus, n+1, minus))
    plus_num = n//plus-len(cummon)
    minus_num = n//minus-len(cummon)
    
    plus = range_sum(n-plus_num+1, n)
    minus = range_sum(1, minus_num)
    
    print(plus - minus)
'''
time complexity: O(t)
for range and set operation O(n)
sum O(1)
'''
