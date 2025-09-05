#구간 합
import sys
input = sys.stdin.readline

n,m = map(int,input().split())
arr=list(map(int,input().split()))
arr2=[0]*(n+1)

for i in range(1,n+1):
    arr2[i]=arr2[i-1]+arr[i-1]
    
for _ in range(m):
    a,b = map(int,input().split())
    print(arr2[b]-arr2[a-1])
