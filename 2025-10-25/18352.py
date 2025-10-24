import sys
from collections import deque

input = sys.stdin.readline

n, m, k, x = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

distance = [-1] * (n + 1)
distance[x] = 0

queue = deque([x])

while queue:
    current_city = queue.popleft()

    for next_city in graph[current_city]:
        if distance[next_city] == -1:
            distance[next_city] = distance[current_city] + 1
            queue.append(next_city)

answer = []
for i in range(1, n + 1):
    if distance[i] == k:
        answer.append(i)

if not answer:
    print(-1)
else:
    for city in answer:
        print(city)
