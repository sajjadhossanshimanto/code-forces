# https://codeforces.com/problemset/problem/1475/A
'''
test case of prime number helped me to figure out the solution
1 can't be considered as odd devisor but if the number is odd
where 1*n = n we can consider n as odd devisor
'''

for _ in range(int(input())):
    n = int(input())

    while n&1==0:# while even
        n = n>>1

    if n>1:
        print("YES")
    else:
        print("NO")
