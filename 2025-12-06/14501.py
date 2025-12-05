import sys
input = sys.stdin.readline

N = int(input())
schedule = [list(map(int, input().split())) for _ in range(N)]

# dp[i]: i번째 날부터 퇴사일까지 얻을 수 있는 최대 수익
dp = [0] * (N + 1)

# 뒤에서부터 거꾸로 계산 (N-1일부터 0일까지)
for i in range(N - 1, -1, -1):
    time, pay = schedule[i]

    # 상담 기간이 퇴사일을 넘기면 상담 불가
    if i + time > N:
        dp[i] = dp[i + 1]
    else:
        # 상담을 안 하는 경우(dp[i+1])와 상담을 하는 경우(pay + dp[i+time]) 중 최댓값 선택
        dp[i] = max(dp[i + 1], pay + dp[i + time])

print(dp[0])