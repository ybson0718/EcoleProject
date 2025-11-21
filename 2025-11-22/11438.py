import sys
from collections import deque

input = sys.stdin.readline
LOG = 18 # 2^17 > 100,000 이므로 18 정도면 충분

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

parent = [[0] * LOG for _ in range(N + 1)]
depth = [0] * (N + 1)
visited = [False] * (N + 1)

# BFS로 트리의 깊이와 바로 위 부모(2^0번째 조상) 설정
def bfs_init(root):
    queue = deque([root])
    visited[root] = True
    while queue:
        node = queue.popleft()
        for child in graph[node]:
            if not visited[child]:
                visited[child] = True
                depth[child] = depth[node] + 1
                parent[child][0] = node 
                queue.append(child)

bfs_init(1)

# 희소 배열(DP) 채우기: 2^i번째 조상 = (2^(i-1)번째 조상)의 2^(i-1)번째 조상
for i in range(1, LOG):
    for j in range(1, N + 1):
        parent[j][i] = parent[parent[j][i - 1]][i - 1]

def lca(a, b):
    # b가 더 깊은 노드가 되도록 스왑
    if depth[a] > depth[b]:
        a, b = b, a
    
    # 깊이 맞추기: 깊이 차이를 2의 제곱수만큼 점프하며 빠르게 좁힘
    for i in range(LOG - 1, -1, -1):
        if depth[b] - depth[a] >= (1 << i):
            b = parent[b][i]
            
    if a == b:
        return a
    
    # LCA 바로 밑까지 공통 조상을 찾아 올라감
    for i in range(LOG - 1, -1, -1):
        if parent[a][i] != parent[b][i]:
            a = parent[a][i]
            b = parent[b][i]
            
    return parent[a][0]

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))