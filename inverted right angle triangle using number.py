#Print inverted right angle triangle using number

num = int(input("Enter the no.of rows : "))

for i in range (num):
    for j in range(num):
        print (j+1,end=" ")
    print()
    num=num-1