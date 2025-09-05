#슬라이딩 윈도우 최소값
from collections import deque
import sys
input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))

dq = deque()  # (idx, val) ; 값 기준 단조 증가 유지

for i in range(N):
    x = arr[i]

    # (A) 뒤에서 현재 값 이상(>=)은 제거 → 단조 증가 유지
    while dq and dq[-1][1] >= x:
        dq.pop()

    # (B) 현재 원소 삽입
    dq.append((i, x))

    # (C) 윈도우에서 벗어난(너무 왼쪽) 원소 제거
    #     윈도우 시작 = i-L+1 이므로, idx <= i-L 이면 범위 밖
    while dq and dq[0][0] <= i - L:
        dq.popleft()

    # (D) 덱 맨 앞의 값이 현재 윈도우 최소
    if i == N - 1:
        print(dq[0][1])          # 마지막은 개행
    else:
        print(dq[0][1], end=' ') # 나머지는 공백으로 구분

