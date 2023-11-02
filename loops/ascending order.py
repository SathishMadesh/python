#Ascending order

a = int (input("Enter the number a : "))
b = int (input("Enter the number b : "))
c = int (input("Enter the number c : "))

if a<=b and b<=c:
    print (a,b,c)
elif b<=c and c<=a:
    print (b,c,a)
elif b<=a and a<=c:
    print (b,a,c)
elif c<=a and a<=b:
    print (c,a,b)
elif c<=b and b<=a:
    print (c,b,a)