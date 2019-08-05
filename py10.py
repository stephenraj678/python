#S
n=int(input())
i=0
while n!=0:
    n=round(n/10)
    i=i+1
if i==0:
    print("1")
else:
    print(i)
