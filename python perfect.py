#perfect 
n=int(input("enter the number”))
sum=1
     for i in range(2,n):
if(n%i==0):
     sum=sum+i
if(sum==n):
    print(n,”is a perfect number”)
else:
    print(n,”is not a perfect number”)
