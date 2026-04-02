import sys
from io import StringIO

# 예제 입력 
# sys.stdin = StringIO('''5 150
# 0 50 10
# 0 50 20
# 50 100 10
# 100 151 10
# 110 140 90
# ''')

sys.stdin = StringIO('''8 900
0 10 9
20 60 45
80 190 100
50 70 15
160 180 14
140 160 14
420 901 5
450 900 0''')

n,d = map(int, sys.stdin.readline().split())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(n)]
INF = 1e9

dist = [INF] * (d+1)
dicts = {}

# 한 칸씩 가는 거 
for i in range(d+1):
    dicts[i] = [[i+1, 1]
]
# 지름길 정보 추가 
for sample in maps:
    s, t, r = sample[0], sample[1], sample[2]
    dicts[s].append([t, r])

visited = [0] * (d+1)

def find_smallest_node(visited, dist):
    min_val = INF
    index = 0

    for i in range(1,d+1):
        if not visited[i] and min_val > dist[i]:
            min_val = dist[i]
            index = i
    return index 


def dijkstra(visited, dist, dicts):
    start = 0
    visited[start] = 1
    dist[0] = 0
    for j in dicts[start]:
        if dist[j[0]] > j[1]:
            dist[j[0]] = j[1]

    for _ in range(d):
        now = find_smallest_node(visited, dist)
        visited[now] = 1
        for s in dicts[now]:
            if s[0] <= d:
                cost = dist[now] + s[1]
                if cost < dist[s[0]]:
                    dist[s[0]] = cost
            
dijkstra(visited, dist, dicts)
print(dist[d])