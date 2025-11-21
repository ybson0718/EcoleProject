import sys
import math

input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))
problem_type = data[0]

# 1부터 N까지 사용할 수 있는 숫자 리스트 초기화
nums = list(range(1, N + 1))

if problem_type == 1:
    K = data[1]
    result = []
    
    for i in range(N):
        # 남은 자리(N-1-i)로 만들 수 있는 경우의 수(팩토리얼) 계산
        fact = math.factorial(N - 1 - i)
        
        # K번째 순열이 되기 위해 현재 숫자 리스트(nums)에서 선택해야 할 인덱스 계산
        step = (K - 1) // fact
        
        result.append(nums[step])
        nums.pop(step) # 사용한 숫자는 리스트에서 제거
        
        # 다음 자릿수를 위해 K값 갱신 (선택한 묶음만큼 뺌)
        K -= fact * step
        
    print(*result)

else:
    target_perm = data[1:]
    result = 1 # 순서는 1번부터 시작하므로 1로 초기화
    
    for num in target_perm:
        fact = math.factorial(N - 1)
        
        # 현재 숫자(num)보다 앞에 올 수 있는(아직 안 쓴) 숫자의 개수만큼 fact를 곱해 더함
        result += nums.index(num) * fact
        
        nums.pop(nums.index(num)) # 사용한 숫자는 제거
        N -= 1 # 남은 자릿수 감소
        
    print(result)