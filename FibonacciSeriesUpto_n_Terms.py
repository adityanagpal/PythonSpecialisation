# generating fibonacci series

n=input("enter the number of terms:")
f=0;s=1;
print(f,s,end=' ')
for i in range(2,int(n)):
   t=f+s
   f=s
   s=t
   print(t,end=' ')
