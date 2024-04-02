n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

j = 0
for i in range(n):
    while j < m and b[j] != a[i]:
        j += 1
if b[j] == a[i] and i == n-1:
    print('Yes')
else:
    print('No')



n,m = list(map(int,input().split()))
a = list(map(int,input().split()))
b = list(map(int,input().split()))

i = 0
j = 0

while i < n and j < m:               # 要通过 i == n来判断是否完成子序列的匹配
    if a[i] == b[j]:
        i += 1
    j += 1
    
if i == n:
    print('Yes')
else:
    print('No')