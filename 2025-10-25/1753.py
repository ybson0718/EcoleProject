import sys
import heapq

input = sys.stdin.readline
INF = sys.maxsize

v, e = map(int, input().split())
start_node = int(input())

graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    u, w, weight = map(int, input().split())
    graph[u].append((w, weight))

def dijkstra(start):
    pq = []
    heapq.heappush(pq, (0, start))
    distance[start] = 0

    while pq:
        dist, current_node = heapq.heappop(pq)

        if distance[current_node] < dist:
            continue

        for next_node, weight in graph[current_node]:
            new_dist = dist + weight
            
            if new_dist < distance[next_node]:
                distance[next_node] = new_dist
                heapq.heappush(pq, (new_dist, next_node))

dijkstra(start_node)

for i in range(1, v + 1):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])
