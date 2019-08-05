n1=int(input())
m=int(input())

new=[]
for i in range(0,n1,1):
    a=int(input())
    new.append(a)
k=0
for j in range(0,m,1):
    k=k+new[j]
print(k)
