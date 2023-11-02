#Print Reverse Right Angle Triangle Pattern with ‘*’ Symbol
num = int(input("Enter the no.of rows : "))

for i in range (num):
    for j in range (num):
        print("*",end=" ")
    print()
    num = num-1