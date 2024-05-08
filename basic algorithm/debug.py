n, m = map(int,input().split())
maze = []
for i in range(n):
    row = list(map(int,input().split()))
    maze.append(row)

def bfs():
    while len(fringe) > 0:
        point = fringe.pop(0)
        if point[:2] == (n-1,m-1):
            print(point[-1])
        for d in direction:
            new = (point[0]+d[0],point[1]+d[1])
            if 0<=new[0]<n and 0<=new[1]<m and new not in visited:
                if not maze[new[0]][new[1]]:
                    visited.add(new)
                    fringe.append(new+(point[-1]+1,))

direction = [(-1,0),(0,1),(1,0),(0,-1)]
fringe = [(0,0,0)]                               # need and another value to determine the path!!!
visited = set()
visited.add((0,0))
path = 0
bfs()