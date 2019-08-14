#S    
n=int(input())
m=list(map(int,input().split()))
d=t=[]
for i in range(0,n):
    d=list(bin(m[i]))
    d=d[2:]
    t.append(d)
t=sorted(t)
t=t[::-1]
for i in range(0,n):
    k=1
    x=0
    for j in range(len(t[i])-1,-1,-1):
        x=x+(int(t[i][j])*k)
        k=k*2
    print(x)
