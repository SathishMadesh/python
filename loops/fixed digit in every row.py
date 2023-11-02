#fixed digit in every row

num = int(input ("enter the number :"))
x=1
for i in range(num):
    for j in range (num):
        print(x,end=" ")
    print ()
    x=x+1