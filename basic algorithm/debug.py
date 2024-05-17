# 2 D
N = 1010
f = [[0 for i in range(N)] for j in range(N)]
v, w = [0] * N, [0] * N

n,m = map(int,input().split())
for i in range(1,n+1):
    v[i], w[i] = map(int,input().split())

for i in range(1,n+1):
    for j in range(1,m+1):
        f[i][j] = f[i-1][j]
        if j >= v[i]:
            f[i][j] = max(f[i][j], f[i-1][j-v[i]] + w[i])
print(f[n][m])

