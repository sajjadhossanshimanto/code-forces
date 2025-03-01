# # https://codeforces.com/contest/2072/problem/B

# for _ in range(int(input())):
#     n = int(input())
#     s = input()

#     dot = [0] * n
#     dot[-1] = int(s[-1] == '-')
#     dash = [0] * n
#     dash[-1] = int(s[-1] == '_')
#     for i in range(n-1, -1, -1):
#         if s[i] == '-':
#             dot[i] = dot[i+1] + 1
#             dash[i] = dash[i+1]
#         else:
#             dot[i] = dot[i+1]
#             dash[i] = dash[i+1] + 1
    
#     # O(n^2) solution would get tle
#     ans = 0
#     for i in range(n):
#         if s[i] == '-':
#             for j in range(i+1, n):
#                 if s[j] == '_':
#                     ans += dot[j]
                    
#             ans += dash[i]

def solve_goblin_price():
    # Read number of test cases
    t = int(input())
    
    for _ in range(t):
        # Read string length and the string itself
        n = int(input())
        s = input().strip()
        
        # Count number of '-' (m) and '_' (k)
        m = s.count('-')
        k = s.count('_')
        
        # If we don't have at least 2 '-' or 1 '_', no "-_-" is possible
        if m < 2 or k < 1:
            print(0)
        else:
            # Maximize subsequences: left '-' * right '-' * '_'
            left = m // 2  # Floor division for left side
            right = (m + 1) // 2  # Ceiling division for right side
            result = left * right * k
            print(result)

# Run the solution
solve_goblin_price()