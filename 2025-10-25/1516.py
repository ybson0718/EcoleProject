import sys
from collections import deque

input = sys.stdin.readline

n = int(input())

graph = [[] for _ in range(n + 1)]
indegree = [0] * (n + 1)
build_time = [0] * (n + 1)
dp_table = [0] * (n + 1)

for i in range(1, n + 1):
    line = list(map(int, input().split()))
    
    build_time[i] = line[0]
    
    for j in range(1, len(line) - 1):
        prereq = line[j]
        graph[prereq].append(i)
        indegree[i] += 1

q = deque()

for i in range(1, n + 1):
    if indegree[i] == 0:
        q.append(i)
        dp_table[i] = 0 

while q:
    current_building = q.popleft()
    
    completion_time = dp_table[current_building] + build_time[current_building]

    for next_building in graph[current_building]:
        dp_table[next_building] = max(dp_table[next_building], completion_time)
        indegree[next_building] -= 1
        
        if indegree[next_building] == 0:
            q.append(next_building)

for i in range(1, n + 1):
    print(dp_table[i] + build_time[i])

