import sys
sys.setrecursionlimit(10**5) # 깊은 트리를 탐색하기 위해 재귀 깊이 해제
input = sys.stdin.readline

N = int(input())
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 각 노드의 부모와 깊이를 저장할 리스트
parent = [0] * (N + 1)
depth = [0] * (N + 1)
visited = [False] * (N + 1)

def dfs(node, d):
    visited[node] = True
    depth[node] = d
    for child in graph[node]:
        if not visited[child]:
            parent[child] = node
            dfs(child, d + 1) # 자식 노드로 내려가며 깊이 1 증가

# 루트 노드(1번)부터 깊이와 부모 계산 시작
dfs(1, 0)

def lca(a, b):
    # 두 노드의 깊이가 다르면, 깊이가 깊은 노드를 위로 올림
    while depth[a] != depth[b]:
        if depth[a] > depth[b]:
            a = parent[a]
        else:
            b = parent[b]
    
    # 깊이를 맞춘 상태에서 두 노드가 같아질 때까지 위로 올림
    while a != b:
        a = parent[a]
        b = parent[b]
        
    return a

M = int(input())
for _ in range(M):
    a, b = map(int, input().split())
    print(lca(a, b))