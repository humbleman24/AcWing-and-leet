
def mergesort(q, l ,r):
    if l >= r:
        return 
    mid = l + r >> 1
    mergesort(q, l, mid)
    mergesort(q, mid + 1, r)
    i, j = l, mid + 1
    pivot = 0
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            temp[pivot] = q[i]
            pivot += 1
            i += 1
        else:
            temp[pivot] = q[j]
            pivot += 1
            j += 1
    while i <= mid:
        temp[pivot] = q[i]
        pivot += 1 
        i += 1
    while j <= r:
        temp[pivot] = q[j]
        pivot += 1
        j += 1
    i = l
    pivot = 0
    while i <= r:
        q[i] = temp[pivot]
        i += 1
        pivot += 1
  

n = int(input())
q = list(map(int,input().split()))
temp = [None] * 100010

mergesort(q,0,n-1)
print(' '.join(map(str,q)))
    