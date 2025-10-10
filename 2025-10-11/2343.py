#기타 레슨
import sys

n, m = map(int, sys.stdin.readline().split())
lectures = list(map(int, sys.stdin.readline().split()))

start = max(lectures) 
end = sum(lectures)   
result = end     

while start <= end:
    mid = (start + end) // 2  
    count = 1          
    current_size = 0  

    for lecture in lectures:
        if current_size + lecture > mid:
            count += 1
            current_size = lecture
        else:
            current_size += lecture
    if count <= m:
        result = mid
        end = mid - 1
    else:
        start = mid + 1

print(result)