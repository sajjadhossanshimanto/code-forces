# # https://codeforces.com/problemset/problem/1374/B

# #%% 
# def prime_factors(n):
#     i = 2
#     flag = True
#     factors = {}
#     while i * i <= n:
#         if i>3:
#             flag = False
#             break

#         if n % i:
#             i += 1
#         else:
#             n //= i
#             factors[i] = factors.get(i, 0) + 1

#     if n > 1:
#         factors[n] = factors.get(n, 0) + 1
#         flag = n in (3, 2)

#     return factors, flag

# for _ in range(int(input())):
#     n = int(input())
#     if n==1:
#         print(0)
#         continue

#     factor, flag = prime_factors(n)
#     factor[2] = factor.get(2, 0)
#     factor[3] = factor.get(3, 0)# setting default keys

#     # print(factor, flag)
#     if not flag:
#         print("-1")
#     elif factor[3]==factor[2]:
#         print(factor[2])
#     elif factor[3]>factor[2]:
#         print(factor[3] - factor[2] + factor[3])
#     elif factor[2]>factor[3]:
#         # print(factor)
#         print(-1)

#%% better style
for _ in range(int(input())):
    n = int(input())
    if n==1:
        print(0)
        continue

    count_3 = 0
    while n%3==0:
        count_3 += 1
        n //= 3
    
    count_2 = 0
    while n%2==0:
        count_2 += 1
        n //= 2
    
    if n > 1 or count_2 > count_3:
        print(-1)
    else:
        print(count_3 - count_2 + count_3)# this will also be true for 3==2
