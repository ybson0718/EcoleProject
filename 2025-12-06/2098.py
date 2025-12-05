import sys
input = sys.stdin.readline
INF = float('inf')

N = int(input())
W = [list(map(int, input().split())) for _ in range(N)]

# dp[현재도시][방문한도시들의비트마스크] = 남은 도시들을 순회하고 출발점으로 돌아오는 최소 비용
dp = [[-1] * (1 << N) for _ in range(N)]

def dfs(now, visited):
    # 모든 도시를 방문했을 경우 (비트가 모두 1인 경우)
    if visited == (1 << N) - 1:
        # 현재 도시에서 출발점(0)으로 가는 길이 있다면 그 비용 반환, 없으면 무한대 반환
        return W[now][0] if W[now][0] > 0 else INF

    # 이미 계산한 적이 있는 상태라면 저장된 값 반환 (메모이제이션)
    if dp[now][visited] != -1:
        return dp[now][visited]

    dp[now][visited] = INF
    
    for next_node in range(1, N):
        # 가는 길이 없고(0)거나 이미 방문했다면 건너뜀
        if W[now][next_node] == 0 or (visited & (1 << next_node)):
            continue
        
        # 다음 도시로 가는 비용 + 그곳에서 남은 도시 순회 비용을 계산해 최솟값 갱신
        dp[now][visited] = min(dp[now][visited], dfs(next_node, visited | (1 << next_node)) + W[now][next_node])

    return dp[now][visited]

# 0번 도시에서 시작, 0번 도시 방문 체크(1) 상태로 탐색 시작
print(dfs(0, 1))