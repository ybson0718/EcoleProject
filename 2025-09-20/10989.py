#수 정렬하기 3
import sys
input = sys.stdin.readline
N = int(input())

counts = [0] * 10001

# N개의 줄에 걸쳐 숫자를 입력받으면서, 해당 숫자의 개수를 1씩 증가시킵니다.
for _ in range(N):
    num = int(input())
    counts[num] += 1

for i in range(1, 10001):
    # 만약 해당 숫자가 한 번이라도 입력되었다면 (counts[i] > 0)
    if counts[i] > 0:
        # 그 개수만큼 해당 숫자(i)를 출력합니다.
        for _ in range(counts[i]):
            print(i)
