#Finding the factors of given number using while loop

num=int(input("Enter the number :"))
i=1
print ("Then factors of",num,"are : ")
while i<=num:
    if (num%i==0):
        print (i,end=" ")
    i=i+1
print ()
    
# for loop

num=int(input("Enter the number :"))

for i in range(1,num+1):
    if num%i==0:
        print (i,end=" ")
        
