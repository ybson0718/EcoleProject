#카드2
from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
dq = deque(range(1, n+1))  # 1부터 n까지 큐에 담기

while len(dq) > 1:
    dq.popleft()           # 제일 위 버림
    dq.append(dq.popleft())  # 다음 카드를 뒤로 옮김

print(dq[0])
