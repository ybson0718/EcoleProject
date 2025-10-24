import sys
from collections import deque

input = sys.stdin.readline

K = int(input())

def solve():
    V, E = map(int, input().split())
    
    graph = [[] for _ in range(V + 1)]
    
    for _ in range(E):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    colors = [0] * (V + 1)
    
    queue = deque()

    for i in range(1, V + 1):
        if colors[i] == 0:
            queue.append(i)
            colors[i] = 1
            
            while queue:
                current_node = queue.popleft()
                
                for next_node in graph[current_node]:
                    if colors[next_node] == 0:
                        colors[next_node] = -colors[current_node]
                        queue.append(next_node)
                    elif colors[next_node] == colors[current_node]:
                        print("NO")
                        return

    print("YES")

for _ in range(K):
    solve()

