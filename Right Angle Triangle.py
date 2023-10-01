# Print Right Angle Triangle pattern with '*' symbol.
num = int (input("Enter the no.of rows : "))
for i in range (num+1):
    for j in range (i):
        print("*",end=" ")
    print ()
    
    
print("\n")
#Print Right AngleTriangle pattern with 'A' Symbol.
num = int (input("Enter the no.of rows : "))
for i in range (num+1):
    for j in range (i):
        print("A",end=" ")
    print ()