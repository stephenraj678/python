#S
from itertools import combinations
(n,x) =input().split()
x=int(x)
arr=[]
comb=combinations(n,len(n)-x)
comb=list(comb)

for i in (comb):
    arr.append("".join(i))

print(min(arr))
