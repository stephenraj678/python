#S
def po(z,n,m):
    s=int(n)-1
    d=int(m)-1
    mi = 0
    x = max(int(z[s]), int(z[d]))
    for i in range(1, x + 1):
        if int(z[s]) % i == 0 and int(z[d]) % i == 0:
            mi = i
    print(mi)

n,m=map(int,input().split())
z=list(map(int,input().split()))
p=[]
for i in range(0,m):
    s=(input())
    p.append(s)
for i in range(0,m):
    if len(p[i])==1:
        print(p[i])
    else:
        po(z,(p[i][0]),(p[i][2]))
