import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

def dfs(node, parent):
    global leaf_count
    
    if node == removed_node:
        return

    children = 0
    for child in graph[node]:
        if child != parent and child != removed_node:
            children += 1
            dfs(child, node)
    
    if children == 0:
        leaf_count += 1

n = int(input())
parents = list(map(int, input().split()))
removed_node = int(input())

graph = [[] for _ in range(n)]
root = -1
leaf_count = 0

for i in range(n):
    if parents[i] == -1:
        root = i
    else:
        graph[i].append(parents[i])
        graph[parents[i]].append(i)

if root == removed_node:
    print(0)
else:
    dfs(root, -1)
    print(leaf_count)