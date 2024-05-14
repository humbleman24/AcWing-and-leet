from collections import deque
N,M = 100010, 100010
h,e,ne,w = [-1]*N, [-1]*N,[-1]*N,[0] * N
idx = 0
dist = [0x3f3f3f] * N
count = [0] * N
dist[1] = 0

def add(a,b,z):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    w[idx] = z
    h[a] = idx
    idx += 1

def spfa():
    visit = set()
    q = deque()
    for i in range(1,n+1):
        q.append(i)
        visit.add(i)
    for i in range(n):
        while len(q):
            point = q.popleft()
            visit.remove(point)
            next = h[point]
            while next != -1:
                j = e[next]
                if dist[j] > dist[point] + w[next]:
                    dist[j] = dist[point] + w[next]
                    count[j] = count[point] + 1
                    if count[j] >= n:
                        return 'Yes'
                    if j not in visit:
                        q.append(j)
                        visit.add(j)
                next = ne[next]
    return 'No'

n,m = map(int,input().split())
for i in range(m):
    a,b,z = map(int,input().split())
    add(a,b,z)

print(spfa())
