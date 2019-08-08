#S
import sys
n = int(input())
if n==1 : print('no')
elif n==2 or n==3 : print('yes')
else :
    for i in range(2,n) :
	if n%i == 0 :
	    print('no')
	    sys.exit()
    else :
	print('yes')
