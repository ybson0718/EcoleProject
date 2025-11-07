import sys

input = sys.stdin.readline

n, m = map(int, input().split())

s = set()
for _ in range(n):
    s.add(input().rstrip())

count = 0
for _ in range(m):
    check_str = input().rstrip()
    if check_str in s:
        count += 1

print(count)