#Print Right Angle Triangle with Continuous Character pattern

num = int (input("Enter the number of rows : "))
a=1
for i in range (1,num+1):
    for j in range (i):
        print (a,end=' ')
        a=a+1
    print ()
    
print("\n") 
# Print Right Angle Triangle with Continuous Character pattern

num = int (input("Enter the number of rows : "))
x = chr(65)
a = 1
for i in range (1,num+1):
    for j in range (i):
        print (x,end=' ')
        x=chr(65+a)
        a=a+1
    print()



