#Min among three numbers

a = int (input("Enter the number a : "))
b = int (input("Enter the number b : "))
c = int (input("Enter the number c : "))

if a<b and b<c:
    print ("a is smaller then b and c")
elif b<a and a<c:
    print ("b is smaller then a and c")
else:
    print ("c is smaller then a and b")