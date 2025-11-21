import sys
import math

input = sys.stdin.readline

N, M, K = map(int, input().split())

# 전체 가능한 문자열의 개수보다 K가 크다면 만들 수 없음 (-1 출력)
if math.comb(N + M, M) < K:
    print(-1)
else:
    result = ""
    while N > 0 and M > 0:
        # 현재 자리에 'a'를 선택했을 때 남은 문자들로 만들 수 있는 경우의 수 계산
        count = math.comb(N - 1 + M, M) 
        
        if K <= count:
            result += "a"
            N -= 1
        else:
            result += "z"
            M -= 1
            K -= count # 'a'로 시작하는 경우의 수를 모두 건너뜀(Skip)

    # 남은 문자들(N이나 M 중 하나가 0이 된 경우)을 뒤에 다 붙여줌
    result += "a" * N + "z" * M
    print(result)