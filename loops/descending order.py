#square pattern with given digit in descending order

num=int(input("Enter the number : "))

x=num
for i in range (num):
    for j in range (num):
        print (x,end=" ")
    print ()
    x=x-1