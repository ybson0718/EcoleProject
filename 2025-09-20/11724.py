import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(v):
    """깊이 우선 탐색(DFS) 함수"""
    visited[v] = True
    for neighbor in graph[v]:
        if not visited[neighbor]:
            dfs(neighbor)

# 정점의 개수(N)와 간선의 개수(M)를 입력받습니다.
try:
    N, M = map(int, input().split())
except ValueError:
    # 입력 줄이 비어있는 경우(N, M이 없는 테스트 케이스)를 대비한 예외 처리
    N, M = 0, 0

graph = [[] for _ in range(N + 1)]
visited = [False] * (N + 1)

for _ in range(M):
    # 2. 안정적인 간선 입력 처리
    line = input().strip()
    if not line: # 빈 줄이 입력되면 무시
        continue
    u, v = map(int, line.split())
    graph[u].append(v)
    graph[v].append(u)

component_count = 0
for i in range(1, N + 1):
    if not visited[i]:
        dfs(i)
        component_count += 1

print(component_count)

