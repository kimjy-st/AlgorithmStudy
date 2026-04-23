import sys
from io import StringIO
from collections import deque

sys.stdin = StringIO('''3 7
32 62
42 68
12 98
95 13
97 25
93 37
79 27
75 19
49 47
67 17''')


N, M = map(int, sys.stdin.readline().split())
roads = {}
for _ in range(N+M):
    x, y = map(int, sys.stdin.readline().split())
    roads[x] = y

visited = [0] * 101
visited[1] = 1

queue = deque()
queue.append(1)
dist = [0] * 101

def bfs(roads, queue, visited):

    while queue:
        cur = queue.popleft()

        if cur == 100:
            print(dist[cur])
            break

        for value in range(1, 7):
            nxt = cur + value

            if nxt > 100 : 
                continue

            if nxt in roads.keys():
                nxt = roads[nxt]

            if not visited[nxt]:
                visited[nxt] = 1
                dist[nxt] = dist[cur] + 1
                queue.append(nxt)


bfs(roads, queue, visited)