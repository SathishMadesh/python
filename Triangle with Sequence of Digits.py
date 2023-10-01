#Print Right Angle Triangle with Sequence of Digits - each row
num = int(input("Enter the no.of rows : "))

for i in range (num+1):
    for j in range (i):
        print (j+1,end=" ")
    print()
    

print("\n")
#Print Right Angle Triangle with Sequence of Alphabet - each row

num = int(input("Enter the no.of rows : "))
for i in range (num+1):
    for j in range(i):
        print (chr(65+j),end=" ")
    print()
    






