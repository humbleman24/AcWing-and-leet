q = list(map(int, input().split()))
k = int(input())

l, r = 0, len(q) - 1
while l < r:
    mid = l + r >> 1
    if q[mid] >= k: r = mid
    else: l = mid + 1
left = l
l, r = 0, len(q) - 1
while l < r:
    mid = l + r + 1 >> 1
    if q[mid] <= k: l = mid
    else: r = mid - 1
right = r

print(left, right)