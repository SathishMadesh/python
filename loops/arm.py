#Finding the entered number is armstrong or not

num = int (input("Enter the number to find which is Armstrong or not : "))
number = num
digit,sum = 0, 0
length = len(str(num))
for i in range (length):
    digit = int(num % 10)
    num = num/10
    sum += pow(digit,length)
if sum == number:
    print ("Entered number is Armstrong")
else:
    print ("Entered number is not an Armstrong")