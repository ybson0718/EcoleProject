#병합정렬
N = int(input())
numbers = []
for _ in range(N):
    numbers.append(int(input()))
        
# 파이썬의 내장 sort() 메서드를 사용하여 리스트를 오름차순으로 정렬합니다.
# 시간 복잡도 O(N log N)을 보장하여 시간 초과 없이 통과할 수 있습니다.
numbers.sort()
    
# 정렬된 결과를 하나씩 출력합니다.
for num in numbers:
    print(num)