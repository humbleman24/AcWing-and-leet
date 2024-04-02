def reverse_pair(q,l,r):
    if l >= r: return 0
    mid = l + r >> 1
    num = reverse_pair(q,l,mid) + reverse_pair(q,mid+1,r)
    i, j, pivot = l, mid+1, 0
    while i <= mid and j <= r:
        if q[i] <= q[j]:
            temp[pivot] = q[i]
            pivot += 1
            i += 1
        else:
            temp[pivot] = q[j]
            pivot += 1
            j += 1
            num += mid - i + 1
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
    return num


n = int(input())
q = list(map(int,input().split()))
temp = [None] * 100010
print(reverse_pair(q,0,n-1))