import sys
input = sys.stdin.readline

x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

# CCW 함수: 세 점의 방향성을 판별 (-1: 시계, 0: 일직선, 1: 반시계)
def ccw(x1, y1, x2, y2, x3, y3):
    temp = (x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)
    if temp > 0: return 1
    elif temp < 0: return -1
    else: return 0

# 네 점에 대한 CCW 값 계산
abc = ccw(x1, y1, x2, y2, x3, y3)
abd = ccw(x1, y1, x2, y2, x4, y4)
cda = ccw(x3, y3, x4, y4, x1, y1)
cdb = ccw(x3, y3, x4, y4, x2, y2)

# 각 선분을 기준으로 상대 선분의 끝점들이 반대 방향에 있는지 확인
# 곱이 0보다 작거나 같다는 것은 서로 반대편에 있거나(음수), 선분 위에 점이 있음(0)을 의미
res1 = abc * abd
res2 = cda * cdb

# 예외 처리: 네 점이 모두 일직선상에 있는 경우 (모든 CCW가 0)
if res1 == 0 and res2 == 0:
    # 좌표 대소 비교를 위해 튜플로 묶어서 정렬 (항상 p1 <= p2, p3 <= p4가 되도록)
    if (x1, y1) > (x2, y2): x1, y1, x2, y2 = x2, y2, x1, y1
    if (x3, y3) > (x4, y4): x3, y3, x4, y4 = x4, y4, x3, y3
    
    # 두 선분이 실제로 포개지는지 확인 (한 선분의 시작점이 다른 선분의 끝점보다 앞서야 함)
    if (x1, y1) <= (x4, y4) and (x3, y3) <= (x2, y2):
        print(1)
    else:
        print(0)

# 일반적인 교차 상태 (T자 형태이거나 서로 가로지르는 경우)
elif res1 <= 0 and res2 <= 0:
    print(1)
else:
    print(0)