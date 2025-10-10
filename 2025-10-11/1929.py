#소수 구하기
import sys
m, n = map(int, sys.stdin.readline().split())

is_prime = [True] * (n + 1)
if n >= 0:
    is_prime[0] = False
if n >= 1:
    is_prime[1] = False

for i in range(2, int(n**0.5) + 1):
    if is_prime[i]:
        for j in range(i * 2, n + 1, i):
            is_prime[j] = False

for i in range(m, n + 1):
    if is_prime[i]:
        print(i)