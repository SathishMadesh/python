#Print inverted Right Angle Triangle with sequence of Alphabets

num = int(input("Enter the no.of rows : "))

for i in range (num):
    for j in range (num):
        print (chr(ord('A')+j),end=' ')
    print ()
    num = num-1
    
print("\n")

#Print Inverted Right Angle Triangle using sequence number in descending order
    
num = int(input("Enter the no.of rows : "))
n=num
for i in range(num):
    for j in range (num):
        print (n-j,end=" ")
    print()
    num=num-1

    