
#Reverse or Inverted Right Angle Triangle using alphabet in descening order

num = int(input("Enter the number of rows : "))
a = chr(ord('A')+num-1)

for i in range (num):
    for j in range (num):
        print (chr(ord(a)-j),end=" ")
    print()
    num=num-1