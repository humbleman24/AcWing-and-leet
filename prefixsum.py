
# one dimension
# n, m = list(map(int,input().split()))
# a = list(map(int,input().split()))
# accumulate = list()                   # calculate the Si ahead then just need one time iteration
# accumulate.append(0)
# for i in range(n):
#     accumulate.append(accumulate[-1] + a[i])
# i = 0
# while i < m:
#     i += 1
#     s,r = list(map(int,input().split()))
#     print(accumulate[r] - accumulate[s-1])


# two dimension
n,m,q = list(map(int,input().split()))
accumulate = list()
accumulate.append([0]*(m+1))                                   # m+1 !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
for i in range(n):
    col = list(map(int,input().split()))
    acc = list()
    acc.append(0)
    for j in range(m):
        acc.append(acc[-1] + col[j])
    for j in range(m+1):
        acc[j] += accumulate[-1][j]
    accumulate.append(acc)

'''another way to calculate the accumulate by using the formula Sij = Si-1j + Sij-1 - Si-1j-1 + aij
accumulate = [[0 for i in range(m+1)] for j in range(n+1)]
for i in range(n):
    col = list(map(int,input().split()))
    for j in range(m):
        accumulate[i+1][j+1] = accumulate[i][j+1] + accumulate[i+1][j] - accumulate[i][j] + col[j]
'''
i = 0
while i < q:
    i += 1
    x1,y1,x2,y2 = list(map(int,input().split()))
    sum = accumulate[x2][y2] - accumulate[x1-1][y2] - accumulate[x2][y1-1] + accumulate[x1-1][y1-1]
    print(sum)