import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] == x:
        return x
    parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    rootA = find_parent(parent, a)
    rootB = find_parent(parent, b)
    
    if rootA < rootB:
        parent[rootB] = rootA
    else:
        parent[rootA] = rootB

n, m = map(int, input().split())
parent = [i for i in range(n + 1)]

for _ in range(m):
    op, a, b = map(int, input().split())
    
    if op == 0:
        union_parent(parent, a, b)
    elif op == 1:
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
