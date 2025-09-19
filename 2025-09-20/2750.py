#수 정렬하기
#n=int(input())
#a=[]
#for i in range(n):
#    a.append(int(input()))
#a.sort()
#for i in a:
#    print(i)

# n개의 수를 입력받음
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))

# --- 버블 정렬 (Bubble Sort) 시작 ---
for i in range(n - 1):
    for j in range(n - 1 - i):
        # 현재 위치의 값(a[j])이 다음 위치의 값(a[j+1])보다 크면
        if a[j] > a[j+1]:
            # 두 값의 자리를 바꿈
            a[j], a[j+1] = a[j+1], a[j]
# --- 버블 정렬 (Bubble Sort) 끝 ---

# 정렬된 결과를 출력
for i in a:
    print(i)