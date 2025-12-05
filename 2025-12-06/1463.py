import sys
input = sys.stdin.readline

N = int(input())

# 연산 횟수를 저장할 dp 테이블 초기화 (인덱스 N까지 사용)
dp = [0] * (N + 1)

for i in range(2, N + 1):
    # 1. 먼저 1을 뺀 경우의 수를 기본값으로 설정
    dp[i] = dp[i - 1] + 1

    # 2. 2로 나누어 떨어지면, 1을 뺀 값과 비교하여 최솟값 갱신
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i // 2] + 1)

    # 3. 3으로 나누어 떨어지면, 현재 값과 비교하여 최솟값 갱신
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i // 3] + 1)

print(dp[N])