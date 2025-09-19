#DFS와 BFS
import sys
from collections import deque

# 빠른 입력을 위해 sys.stdin.readline을 사용합니다.
input = sys.stdin.readline

def bfs(start_v):
    # 탐색 순서를 저장할 리스트
    visit_order = []
    
    # 큐를 생성하고 시작 정점을 추가합니다.
    q = deque([start_v])
    
    # 시작 정점을 방문 처리합니다.
    visited[start_v] = True

    # 큐가 비어있지 않은 동안 반복합니다.
    while q:
        # 큐의 맨 앞에서 정점을 하나 꺼냅니다.
        v = q.popleft()
        visit_order.append(v)
        
        # 현재 정점과 연결된 다른 정점들을 확인합니다.
        for neighbor in graph[v]:
            # 만약 아직 방문하지 않은 정점이라면
            if not visited[neighbor]:
                # 큐에 추가하고 방문 처리합니다.
                q.append(neighbor)
                visited[neighbor] = True
    
    return visit_order

def dfs(v):
    # 현재 정점을 방문 처리하고 탐색 순서에 추가합니다.
    visited[v] = True
    dfs_visit_order.append(v)
    
    # 현재 정점과 연결된 다른 정점들을 확인합니다.
    for neighbor in graph[v]:
        # 만약 아직 방문하지 않은 정점이라면
        if not visited[neighbor]:
            # 해당 정점으로 재귀 호출하여 탐색을 계속합니다.
            dfs(neighbor)

# --- 메인 로직 ---

# 정점의 개수(N), 간선의 개수(M), 시작 정점(V)을 입력받습니다.
N, M, V = map(int, input().split())

# 그래프를 인접 리스트 방식으로 표현합니다.
graph = [[] for _ in range(N + 1)]

# M개의 간선 정보를 입력받아 그래프를 구성합니다.
for _ in range(M):
    u, v = map(int, input().split())
    # 방향 없는 그래프이므로 양쪽에 모두 추가합니다.
    graph[u].append(v)
    graph[v].append(u)

# "정점 번호가 작은 것을 먼저 방문" 조건을 만족시키기 위해
# 각 정점의 인접 리스트를 오름차순으로 정렬합니다.
for i in range(1, N + 1):
    graph[i].sort()

# --- DFS 실행 ---
visited = [False] * (N + 1) # 방문 기록 리스트 초기화
dfs_visit_order = []
dfs(V)
print(*dfs_visit_order)

# --- BFS 실행 ---
visited = [False] * (N + 1) # 방문 기록 리스트 초기화
bfs_visit_order = bfs(V)
print(*bfs_visit_order)
