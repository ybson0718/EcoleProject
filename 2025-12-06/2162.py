import sys
input = sys.stdin.readline

# CCW 알고리즘: 세 점의 방향성을 판별 (외적 활용)
def ccw(x1, y1, x2, y2, x3, y3):
    tmp = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if tmp > 0: return 1
    elif tmp < 0: return -1
    return 0

# 두 선분(l1, l2)이 교차하는지 확인하는 함수
def is_cross(l1, l2):
    x1, y1, x2, y2 = l1
    x3, y3, x4, y4 = l2

    # 각 선분을 기준으로 다른 선분의 끝점들이 어느 방향에 있는지 확인
    abc = ccw(x1, y1, x2, y2, x3, y3) * ccw(x1, y1, x2, y2, x4, y4)
    cdab = ccw(x3, y3, x4, y4, x1, y1) * ccw(x3, y3, x4, y4, x2, y2)

    # 두 선분이 일직선 상에 있을 때 (CCW 값이 모두 0)
    if abc == 0 and cdab == 0:
        # 좌표 비교를 위해 정렬 (시작점이 끝점보다 작도록)
        if (x1, y1) > (x2, y2): x1, y1, x2, y2 = x2, y2, x1, y1
        if (x3, y3) > (x4, y4): x3, y3, x4, y4 = x4, y4, x3, y3
        # 선분이 실제로 겹치는지 구간 확인
        return (x1, y1) <= (x4, y4) and (x3, y3) <= (x2, y2)
    
    # 일반적인 교차 상태 (두 선분이 서로를 가로지름)
    return abc <= 0 and cdab <= 0

# Union-Find: 부모 노드 찾기 (Path Compression)
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])
    return parent[x]

# Union-Find: 두 그룹 합치기
def union(a, b):
    a = find(a)
    b = find(b)
    if a != b:
        parent[b] = a

N = int(input())
lines = [list(map(int, input().split())) for _ in range(N)]
parent = [i for i in range(N)]

# 모든 선분 쌍을 비교 (O(N^2))
for i in range(N):
    for j in range(i + 1, N):
        if is_cross(lines[i], lines[j]):
            union(i, j)

# 모든 노드의 최종 부모를 갱신
parent = [find(i) for i in range(N)]

# 그룹의 개수와 가장 큰 그룹의 크기 계산
group_count = len(set(parent))
max_group_size = max([parent.count(i) for i in set(parent)])

print(group_count)
print(max_group_size)