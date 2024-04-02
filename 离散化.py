n,m = list(map(int,input().split()))
N = 300010

a = [0 for i in range(N)]
s = [0 for i in range(N)]
index = list()
add = list()
query = list()

for i in range(n):
    x,c = list(map(int,input().split()))
    index.append(x)
    add.append((x,c))
for j in range(m):
    l,r = list(map(int,input().split()))
    index.append(l)
    index.append(r)
    query.append((l,r))

index.sort()
index = list(set(index))

def find(x):
    l = 0
    r = len(index) - 1
    while l < r:
        mid = l + r >> 1
        if index[mid] >= x:
            r = mid
        else:
            l = mid + 1
    return r + 1

for x,c in add:
    x = find(x)
    a[x]+=c

for i in range(1,len(index)+1):
    s[i] = s[i-1] + a[i]

for l,r in query:
    l = find(l)
    r = find(r)
    print(s[r] - s[l-1])
