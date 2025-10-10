# 동전 0
import sys

def find(coin, price):
    num = 0
    tmp = price
    for i in reversed(coin):
        num += tmp // i
        tmp %= i
    return num


n, price = map(int, sys.stdin.readline().strip().split())
coin = [int(input()) for _ in range(n)]
print(find(coin, price))