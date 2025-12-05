import sys
input = sys.stdin.readline

x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

# 외적(Cross Product) 공식 적용: (x2-x1)(y3-y1) - (x3-x1)(y2-y1)
result = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)

if result > 0:   # 양수면 반시계 방향
    print(1)
elif result < 0: # 음수면 시계 방향
    print(-1)
else:            # 0이면 일직선
    print(0)