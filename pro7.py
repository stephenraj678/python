#S
n=int(input())
m=1000
for i in range(0,20):
    if pow(2,i)<=n:
        x = abs(pow(2, i) - n)
        if x < m: m = x
print(m)
