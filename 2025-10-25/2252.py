import sys
from collections import deque

input = sys.stdin.readline

n, m = map(int, input().split())

indegree = [0] * (n + 1)
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

def topology_sort():
    result = []
    q = deque()

    for i in range(1, n + 1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        current_student = q.popleft()
        result.append(current_student)

        for next_student in graph[current_student]:
            indegree[next_student] -= 1
            
            if indegree[next_student] == 0:
                q.append(next_student)

    print(*result)

topology_sort()

