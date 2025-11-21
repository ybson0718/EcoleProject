import sys
input = sys.stdin.readline

N, K = map(int, input().split())

# 2차원 배열(DP 테이블) 초기화: (N+1) x (N+1) 크기
D = [[0 for _ in range(N + 1)] for _ in range(N + 1)]

# 초기값 설정
for i in range(N + 1):
    D[i][1] = i
    D[i][0] = 1
    D[i][i] = 1

# DP 점화식 적용 (파스칼의 삼각형)
for i in range(2, N + 1):
    for j in range(1, i): # 자바 코드의 j < i 조건과 동일
        # 조합 기본 점화식: nCr = n-1Cr + n-1Cr-1
        D[i][j] = D[i - 1][j] + D[i - 1][j - 1]

print(D[N][K])