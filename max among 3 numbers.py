#Max among three numbers

a = int (input("Enter the number a : "))
b = int (input("Enter the number b : "))
c = int (input("Enter the number c : "))

if a>b and b>c:
    print ("a is grater then b and c")
elif b>a and a>c:
    print ("b is grater then a and c")
else:
    print ("c is greater then a and b")