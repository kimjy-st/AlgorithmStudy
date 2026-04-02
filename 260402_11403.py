import sys
from io import StringIO
# 예시 입력
# sys.stdin = StringIO('''3
# 0 1 0
# 0 0 1
# 1 0 0
# ''')

sys.stdin = StringIO('''7
0 0 0 1 0 0 0
0 0 0 0 0 0 1
0 0 0 0 0 0 0
0 0 0 0 1 1 0
1 0 0 0 0 0 0
0 0 0 0 0 0 1
0 0 1 0 0 0 0''')

INF = 1e9
N = int(sys.stdin.readline())
maps = [list(map(int, sys.stdin.readline().split())) for _ in range(N)]



def find_smallest_node(dist, visited):
    min_val = INF
    index=0
    for i in range(1, N):
        if dist[i] < min_val and not visited[i]:
            min_val = dist[i]
            index = i
    return index

def dijkstra(start, dist, visited):
    dist[start] = 0
    visited[start] = 0 
    # 이 문제에선 시작점이라도 visited 체크 안함
    # 답변 예시에서 대각 성분이 0인 것도 있음 아마 돌아올 수 있냐를 보는듯 
    for idx, j in enumerate(maps[start]):
        # 갈 수 있는 곳일 때 거리 업데이트 
        dist[idx] = j if j != 0 else INF

    for _ in range(N-1):
        now = find_smallest_node(dist, visited)
        visited[now] = True

        for idx, j in enumerate(maps[now]):
            # 갈 수 있는 곳만 dist 업데이트 
            cost = dist[now] + j if j!=0 else INF
            if cost < dist[idx]:
                dist[idx] = cost

        

for start in range(N):
    dist = [1e9] * (N)
    visited = [0]*(N)
    dijkstra(start, dist, visited)
    
    answer = ''
    for d in dist:
        if d < INF:
            if d >0 :
                answer += '1 '
            else:
                answer += '0 '
        else:
            answer += '0 '
    print(answer)