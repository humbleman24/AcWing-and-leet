# find the kth number of the sorted array

n, k = list(map(int,input().split()))
q = list(map(int,input().split()))


def quickselect(l,r,k):
    if l == r:
        return q[l]
    x = q[l+r >> 1]
    i = l - 1
    j = r + 1
    while i < j:
        i += 1
        while q[i] < x:
            i += 1
        j -= 1
        while q[j] > x:
            j -= 1
        
        if i < j:
            q[i], q[j] = q[j], q[i]
    sl = j - l + 1
    if k <= sl:
        return quickselect(l, j, k)
    else:
        return quickselect(j+1, r, k - sl)
    
print(quickselect(0,n - 1,k))

