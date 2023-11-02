#Print Right Angle Triangle with Fixed Alphabet Symbol

num = int(input ("Enter the number of rows : "))

for i in range(num+1):
    for j in range (i):
        print (chr(64+i),end=" ")
    print ()
    
print("\n")
#Print right angle triangle with fixed digit symbol in every row
num = int(input ("Enter the no.of rows : "))
for i in range (num+1):
    for j in range(i):
        print(i,end = " ")
    print ()
