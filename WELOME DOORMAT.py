m,n = map(int,input().split())
a=((n-1)//2)-1
b=((m+1)//2)
c=((n+1)//2)
times=1
number=0
x=''
s='.|.'
for i in range(1,m+1):
   if(i<b):
       print(a*'-',end=((times*s)+a*'-'))
       print('\r')
       a=a-3
       times=times+2
   elif(i==b):
       for j in range(1,(c-3)):
           number=number+1
       print(number*'-',end=("WELCOME"+number*'-'))
       print('\r')
   else:
       a=a+3
       times=times-2
       print(a*'-',end=((times*s)+a*'-'))
       print('\r')
