#소트인사이드

# n개의 수를 입력받음
n = list(map(int, input()))

# --- 선택 정렬 (Selection Sort) 시작 ---
for i in range(len(n)):
    # 현재 위치(i)를 최댓값의 위치로 우선 지정
    max_index = i
    
    # 현재 위치(i) 다음부터 마지막 값까지 반복하며
    for j in range(i + 1, len(n)):
        # 더 큰 값을 찾으면, 그 위치를 최댓값의 위치로 변경
        if n[j] > n[max_index]:
            max_index = j
            
    # 찾은 최댓값(n[max_index])과 현재 위치의 값(n[i])을 서로 교환
    n[i], n[max_index] = n[max_index], n[i]

for i in n:
    print(i, end='')