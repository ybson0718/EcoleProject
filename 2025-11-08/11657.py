import sys

input = sys.stdin.readline
INF = sys.maxsize

n, m = map(int, input().split())
edges = []
distance = [INF] * (n + 1)

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

def bellman_ford(start):
    distance[start] = 0

    # N번 반복 (N-1번 갱신 + 1번 음수 사이클 확인)
    for i in range(n):
        for j in range(m):
            current_node, next_node, cost = edges[j]

            if distance[current_node] != INF and distance[next_node] > distance[current_node] + cost:
                distance[next_node] = distance[current_node] + cost
                
                # N번째 반복에서도 갱신이 발생하면 음수 사이클 존재
                if i == n - 1:
                    return True  
                    
    return False

has_negative_cycle = bellman_ford(1)

if has_negative_cycle:
    print("-1")
else:
    for i in range(2, n + 1):
        if distance[i] == INF:
            print("-1")
        else:
            print(distance[i])