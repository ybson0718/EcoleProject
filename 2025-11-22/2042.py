import sys
input = sys.stdin.readline

def update(i, diff):
    while i <= N:
        tree[i] += diff
        # 비트 연산을 통해 현재 노드가 포함된 다음 구간(부모/오른쪽)으로 이동
        i += (i & -i)

def prefix_sum(i):
    result = 0
    while i > 0:
        result += tree[i]
        # 비트 연산을 통해 0이 될 때까지 구간 합을 누적하며 이동
        i -= (i & -i)
    return result

def interval_sum(start, end):
    # 구간 합 공식: (1~end까지의 합) - (1~start-1까지의 합)
    return prefix_sum(end) - prefix_sum(start - 1)

N, M, K = map(int, input().split())

arr = [0] * (N + 1)
tree = [0] * (N + 1)

for i in range(1, N + 1):
    x = int(input())
    arr[i] = x
    update(i, x)

for _ in range(M + K):
    a, b, c = map(int, input().split())
    
    if a == 1:
        diff = c - arr[b] # 바뀐 값과 기존 값의 차이를 계산
        arr[b] = c        # 원본 배열 값 갱신 (다음 차이 계산을 위해)
        update(b, diff)   # 차이만큼만 트리 갱신
    else:
        print(interval_sum(b, c))