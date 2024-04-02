

def binarysearch(q,n,k):
    l, r = 0, n-1
    while l < r:
        mid = l + r >> 1    #  update the mid
        if q[mid] >= k:
            r = mid
        else:
            l = mid + 1
    if q[l] != k: 
        return '-1 -1'
    else: left = l



    
    l, r = 0, n-1
    while l<r:
        mid = l + r + 1 >> 1        # plus one
        if q[mid] <= k:
            l = mid
        else:
            r = mid -1
    return '{} {}'.format(left,l)

n,m = list(map(int,input().split()))
q = list(map(int,input().split()))

while m > 0:
    m -= 1
    k = int(input())
    print(binarysearch(q,n,k))

    