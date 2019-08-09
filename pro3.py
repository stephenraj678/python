#S
sa,se=input().split()
r=abs(len(sa)-len(se))
for i in range(len(sa)):
    if len(se)==1 and se[i] in sa:
        break
    if sa[i]!=se[i]:
        r+=1
print(r)
