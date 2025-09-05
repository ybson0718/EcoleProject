#좋다
import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.sort()

good = 0

for i in range(n):
    target = arr[i]
    l, r = 0, n - 1
    found = False

    while l < r:
        if l == i:
            l += 1
            continue
        if r == i:
            r -= 1
            continue

        s = arr[l] + arr[r]
        if s == target:
            found = True
            break
        elif s < target:
            l += 1
        else:
            r -= 1

    if found:
        good += 1

print(good)
