
num = int (input("Enter the number : "))

n1,n2 = 0,1

if num < 0:
    print ("Enter the positive value")
elif num==1:
    print ("Fibonacci series upti",num,"is :",n1)
else:
    print ("Fibonacci series upti",num,"is :")
    while n1 < num:
        print (n1, end=" ")
        nth = n1 + n2
        n1 = n2
        n2 = nth
        