#S
def high(max,l):
    t=[]
    for i in range(0,min(len(max),len(l))):
        if max[i]==l[i]:
            t.append(l[i])
        else: break
    return t
n=int(input())
l=[]
for i in range(0,n):
    s=input()
    l.append(s)
max=[]
max=l[0]
for i in range(1,n):
    max=high(max,l[i])
for i in range(0,len(max)):
    print(max[i],end="")
