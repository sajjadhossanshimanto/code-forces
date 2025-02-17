
def range_sum(l, r):
    if l==0: return pre_sum[r]

    return pre_sum[r]-pre_sum[l-1]

for _ in range(int(input())):
    n = int(input())
    arr = list(map(int, input().split()))

    pre_sum = [abs(arr[0])]
    for i in range(1, n):
        pre_sum.append(pre_sum[-1]+abs(arr[i]))
    
    total = 0
    l = 0
    r = n-1
    while l<r:#TODO: need to handle where l==r
        if arr[l]>0:
            total+=abs(arr[l])
            l+=1
        if arr[r]<0:
            total+=abs(arr[r])
            r-=1
        else:
            lcur = l
            while not arr[lcur]>0:
                lcur +=1
                if lcur==r:
                    lcur=l
                    break
            
            rcur = r
            while not arr[rcur]<0:
                rcur -=1
                if rcur==l:
                    rcur=r
                    break

            rsum = range_sum(rcur, r)
            lsum = range_sum(l, lcur)
            if rsum>lsum:
                r = rcur-1
                total+=rsum
            else:
                l = lcur+1
                total+=lsum

    print(total)
