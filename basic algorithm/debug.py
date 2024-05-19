N = 1010
f = [[0 for i in range(N)] for j in range(N)]
arrs = [0] * N
n, m = map(int,input().split())
for i in range(n):
    arrs[i] = [0] + list(input())


def edit_dist(a,b):
    for i in range(len(b)): f[0][i] = i
    for i in range(len(a)): f[i][0] = i

    for i in range(1, len(a)):
        for j in range(1, len(b)):
            if a[i] != b[j]:
                f[i][j] = min(f[i-1][j], f[i][j-1], f[i-1][j-1]) + 1
            else:
                f[i][j] = min(f[i-1][j] + 1, f[i][j-1] + 1, f[i-1][j-1])
    return f[len(a)-1][len(b)-1]

for i in range(m):
    q,s = input().split()
    q, s = [0] + list(q), int(s)
    res = 0
    for j in range(n):
        arr = arrs[j]
        if edit_dist(arr,q) <= s:
            res += 1
    print(res)
        
