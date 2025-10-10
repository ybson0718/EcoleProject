# 카드 정렬하기
import sys
import heapq

n = int(sys.stdin.readline())

heap = []
for _ in range(n):
    heapq.heappush(heap, int(sys.stdin.readline()))

total_comparisons = 0

while len(heap) > 1:
    deck1 = heapq.heappop(heap)
    deck2 = heapq.heappop(heap)

    current_sum = deck1 + deck2

    total_comparisons += current_sum

    heapq.heappush(heap, current_sum)

print(total_comparisons)