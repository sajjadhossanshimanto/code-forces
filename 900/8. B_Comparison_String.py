# #%% failed attempt 1
# for _ in range(int(input())):
#     n = int(input())
#     s = input()

#     ini = 50
#     counter = set([ini])
#     for i in s:
#         if i=="<":
#             ini += 1
#         else:
#             ini -= 1
#         counter.add(ini)
    
#     print(len(counter))

# #%% failed attempt 2
# for _ in range(int(input())):
#     n = int(input())
#     s = input()

#     ini = 50
#     counter = set([ini])
#     prev = ini
#     for i in s:
#         if i=="<":
#             prev += 1
#         else:
#             prev = ini
#         counter.add(prev)
    
#     print(len(counter))

#%%
for _ in range(int(input())):
    n = int(input())
    s = input()

    mx_ln = 0
    prev = ""
    ln = 1
    for i in s:
        if i==prev:
            ln += 1
        else:
            mx_ln = max(mx_ln, ln) # counting maximum consequtive of any sign
            prev = i
            ln = 1
    
    print(max(mx_ln, ln)+1)