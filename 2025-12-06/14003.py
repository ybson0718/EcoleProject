import sys
from bisect import bisect_left
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

# LIS 길이를 구하기 위한 배열 (실제 LIS가 아님에 주의)
lis_arr = [A[0]]
# (LIS 배열 내 인덱스, 실제 값)을 저장하여 나중에 역추적할 기록용 리스트
record = [(0, A[0])]

for i in range(1, N):
    if A[i] > lis_arr[-1]:
        # 현재 값이 가장 큰 값보다 크면 뒤에 붙임
        lis_arr.append(A[i])
        record.append((len(lis_arr) - 1, A[i]))
    else:
        # 그렇지 않으면 이분 탐색으로 들어갈 자리를 찾아 교체 (길이 유지, 최솟값 갱신)
        idx = bisect_left(lis_arr, A[i])
        lis_arr[idx] = A[i]
        record.append((idx, A[i]))

# 1. LIS 길이 출력
print(len(lis_arr))

# 2. 뒤에서부터 역추적하여 실제 수열 찾기
result = []
target_idx = len(lis_arr) - 1

for i in range(N - 1, -1, -1):
    # 기록된 인덱스가 찾으려는 인덱스와 같다면 정답 수열에 포함
    if record[i][0] == target_idx:
        result.append(record[i][1])
        target_idx -= 1

# 역순으로 담았으므로 뒤집어서 출력
print(*result[::-1])