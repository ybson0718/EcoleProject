import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

n, m, k = map(int, input().split())
graph = [[] for _ in range(n + 1)]
distance = [[] for _ in range(n + 1)]

for _ in range(m):
    u, v, weight = map(int, input().split())
    graph[u].append((v, weight))

def dijkstra_kth(start):
    pq = [] 
    heapq.heappush(pq, (0, start))
    heapq.heappush(distance[start], 0)

    while pq:
        dist, current_node = heapq.heappop(pq)

        for next_node, weight in graph[current_node]:
            new_dist = dist + weight
            
            if len(distance[next_node]) < k:
                heapq.heappush(distance[next_node], -new_dist)
                heapq.heappush(pq, (new_dist, next_node))
            elif new_dist < -distance[next_node][0]:
                heapq.heapreplace(distance[next_node], -new_dist)
                heapq.heappush(pq, (new_dist, next_node))

dijkstra_kth(1)

for i in range(1, n + 1):
    if len(distance[i]) < k:
        print(-1)
    else:
        print(-distance[i][0])
