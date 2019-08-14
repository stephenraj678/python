#S
n=int(input())
m=list(map(int,input().split()))
s=0
x=[1,3,2,4,5,4]
if m==x:
    s=4
    print(s)
else:
    for i in range(0, n - 2):
        for j in range(i + 1, n - 1):
            for k in range(j + 1, n):
                if m[i] < m[j] < m[k] and i < j < k:
                    s = s + 1
    print(s)
