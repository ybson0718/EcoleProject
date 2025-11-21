import sys
sys.setrecursionlimit(10**6) # 재귀 깊이 제한 해제 (기본값은 1000이라 부족할 수 있음)
input = sys.stdin.readline

N, K = map(int, input().split())
dp = [[-1] * (N + 1) for _ in range(N + 1)] # 계산되지 않은 값은 -1로 초기화

def bino(n, k):
    # 기저 사례: k=0(아무것도 안 뽑음)이거나 n=k(모두 뽑음)인 경우 경우의 수는 1
    if k == 0 or n == k:
        return 1
    
    # 이미 계산한 적이 있다면(메모이제이션), 저장된 값을 바로 반환
    if dp[n][k] != -1:
        return dp[n][k]
    
    # 파스칼의 법칙: nCk = (n-1)C(k-1) + (n-1)Ck
    dp[n][k] = (bino(n - 1, k - 1) + bino(n - 1, k)) % 10007
    
    return dp[n][k]

print(bino(N, K))