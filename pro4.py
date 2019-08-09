#S    
k,j=map(str,input().split())
s=0
if len(k)>len(j):
  k,j=j,k
i=0
while i<len(k):
  s+=(ord(j[i])-ord(k[i]))
  i+=1
for i in range(i,len(j)):
  s+=ord(j[i])-ord('a')+1
print(s)
