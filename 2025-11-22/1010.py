import sys
import math

input = sys.stdin.readline

T = int(input())

for _ in range(T):
    N, M = map(int, input().split())
    
    # M개의 사이트 중 N개를 선택하는 조합(nCr) 계산
    # 순서가 정해져 있으므로(겹치지 않음) 뽑기만 하면 됨
    print(math.comb(M, N))