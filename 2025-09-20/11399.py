#ATM
n=int(input())
m=list(map(int,input().split()))
m.sort()
total=0
sum=0
for i in range(n):
    sum+=m[i]
    total+=sum
print(total)

