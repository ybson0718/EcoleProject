#수들의 합

import sys
input =sys.stdin.readline
n=int(input())
count=0
s=0
for i in range(0,n):
    s=0
    for j in range(i,n):
        s+=j
        if s==n:
            count+=1
            break
        elif s>n:
            break
print(count)

#수들의 합
import sys
input = sys.stdin.readline

n = int(input())
count = 0

left, right = 1, 1
s = 1  # 현재 구간 [left, right]의 합

while right <= n:
    if s == n:
        count += 1
        # 다음 경우 탐색을 위해 왼쪽을 줄여 합을 감소
        s -= left
        left += 1
    elif s < n:
        # 합이 부족 → 오른쪽 확장
        right += 1
        if right > n:   # 더 이상 확장 불가
            break
        s += right
    else:  # s > n
        # 합이 큼 → 왼쪽을 줄여 합을 감소
        s -= left
        left += 1

print(count)

        
    