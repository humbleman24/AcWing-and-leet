# use heap to maintain the smallest point to expand in the next iteration.
from queue import PriorityQueue

N = 150010
h, e, ne, w = [-1] * N, [-1] * N, [-1] * N, [0] * N
idx = 0
q = PriorityQueue()
visit = set()
dist = [0x3f3f3f,0] + [0x3f3f3f] * N

def add(a,b,z):
    global idx
    e[idx] = b
    ne[idx] = h[a]
    w[idx] = z
    h[a] = idx
    idx += 1

def dijkstra():
    q.put((dist[1],1))
    while not q.empty():
        d, var = q.get()
        if var in visit: continue          # important
        visit.add(var)
        next = h[var]
        while next != -1:
            j = e[next]
            if dist[j] > d + w[next]:
                dist[j] = d + w[next]
                q.put((dist[j],j))
            next = ne[next]
    if dist[n] == 0x3f3f3f:
        return -1
    return dist[n]




n,m = map(int,input().split())
for i in range(m):
    a,b,z = map(int,input().split())
    add(a,b,z)

print(dijkstra())
