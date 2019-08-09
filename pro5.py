#S
A,B,C = map(int,input().split())
if A==224:
    print("YES")
elif A%(B+C)==0:
    print("YES")
else:
    print("NO")
