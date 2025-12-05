import sys
input = sys.stdin.readline

n, m = map(int, input().split())
board = [list(map(int, list(input().strip()))) for _ in range(n)]

max_side = 0

for i in range(n):
    for j in range(m):
        # 행과 열이 0보다 크고, 현재 칸이 1일 때만 DP 수행 (첫 행/열은 계산 불가)
        if i > 0 and j > 0 and board[i][j] == 1:
            # 왼쪽, 위쪽, 왼쪽 대각선 위 중 가장 작은 값에 1을 더해 현재 최대 변의 길이 저장
            board[i][j] += min(board[i][j-1], board[i-1][j], board[i-1][j-1])
            
        # 갱신된 변의 길이 중 최댓값을 계속 추적
        max_side = max(max_side, board[i][j])

# 넓이를 구해야 하므로 변의 길이를 제곱해서 출력
print(max_side ** 2)