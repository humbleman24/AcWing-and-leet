# # One dimension
n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
# construct the difference matrix
b = [0]*n
for i in range (n-1):
    b[i] += a[i]
    b[i+1] -= a[i]
b[-1] += a[-1]
# b = [a[0]]
# b += [a[i+1] - a[i] for i in range(0,n-1)]
i = 0
while i < m:
    i += 1
    l,r,c = list(map(int,input().split()))
    b[l-1] += c
    if r == n:
        continue
    b[r] -= c
out = [0]
for i in range(n):
    out.append(out[-1]+b[i])
    print(out[-1],end=' ')



# two dimension
n,m,q = list(map(int,input().split()))
b = [[0 for i in range(m)] for j in range(n)]
for i in range(n-1):
    col = list(map(int,input().split()))
    for j in range(m-1):
        b[i][j] += col[j]
        b[i][j+1] -= col[j]
        b[i+1][j] -= col[j]
        b[i+1][j+1] += col[j]
    b[i][-1] += col[-1]
    b[i+1][-1] -= col[-1]
col = list(map(int,input().split()))
for j in range(m-1):
    b[-1][j] += col[j]
    b[-1][j+1] -= col[j]
b[-1][-1] += col[-1]    

i = 0
while i < q:
    i += 1
    x1,y1,x2,y2,c = list(map(int,input().split()))
    x1,y1,x2,y2 = x1-1,y1-1,x2-1,y2-1
    b[x1][y1] += c
    if y2 < m-1:
        b[x1][y2+1] -= c                            # +1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if x2 < n-1:
        b[x2+1][y1] -= c                            # +1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
    if y2 < m-1 and x2 < n-1:
        b[x2+1][y2+1] += c                          # +1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

a = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(1,n+1):
    for j in range(1,m+1):
        a[i][j] = a[i][j-1] + a[i-1][j] - a[i-1][j-1] + b[i-1][j-1]
        print(a[i][j], end=' ')
    print()




