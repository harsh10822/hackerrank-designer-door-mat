#m=int(input("Enter length: "))#rows
#n=int(input("Enter width:  "))#columns
#g,h=(input("Enter length: ")).split()
#m=int(g)
#n=int(h)
m, n = [int(m) for m in input("Enter two value: ").split()]
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










































'''for j in range(1,m+1):
    if(j<((m-1)//2)):
        for i in range(1,(n+1)):
            if(i!=((n-1))//2 and i!=(d-2)):
                a=a+'-'
                print('-',end='')
            else:
                print((c*s)+a,end='\n')
                c=c+2
                d=d-2
    elif(j==((m-1)//2)):
        print("WELOME")
    #else:
     #   for k in range(1,n+1):
            


'''
















'''while c!=((m-1)//2):
    for i in range(1,n+1):
        if((n%2)!=0):#if n is an odd no.
            if(i!=((n-1)//2)):#if not centre 
                print('-',end='')
            else:
                print(s)
    c=c+2
else:
    print("WELCOME")
'''
