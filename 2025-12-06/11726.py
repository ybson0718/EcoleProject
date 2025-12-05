import sys
input = sys.stdin.readline

n = int(input())

# n은 최대 1,000이므로 넉넉하게 배열 생성 (인덱스 에러 방지)
dp = [0] * 1001

# 초기값 설정: 2x1은 1가지(세로1), 2x2는 2가지(세로2, 가로2) 방법 존재
dp[1] = 1
dp[2] = 2

for i in range(3, n + 1):
    # 점화식: 마지막에 '세로 막대 1개(2x1)'가 오는 경우 + '가로 막대 2개(1x2)'가 오는 경우
    dp[i] = (dp[i-1] + dp[i-2]) % 10007

print(dp[n])