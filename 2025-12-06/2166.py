import sys
input = sys.stdin.readline

N = int(input())
points = [list(map(int, input().split())) for _ in range(N)]

# 신발끈 공식을 적용하기 위해 마지막에 시작점을 추가하여 닫힌 도형으로 만듦
points.append(points[0])

x_sum = 0
y_sum = 0

for i in range(N):
    # (x_i * y_i+1)의 합 계산 (↘ 방향 대각선 곱)
    x_sum += points[i][0] * points[i+1][1]
    
    # (y_i * x_i+1)의 합 계산 (↙ 방향 대각선 곱)
    y_sum += points[i][1] * points[i+1][0]

# 공식: 1/2 * |(↘ 방향 합) - (↙ 방향 합)|
area = abs(x_sum - y_sum) / 2

# 소수점 첫째 자리까지 출력
print(f"{area:.1f}")