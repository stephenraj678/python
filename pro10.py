#s
n=int(input())
s=0
m=list(map(int,input().split()))
for i in range(0,n-1):
    for j in range(0,n):
        if m[i]<m[j]:
            s=s+(i+1)
print(s)
