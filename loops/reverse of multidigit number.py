#print the reverse of multidigit number

num = int(input("Enter the multi digit value : "))

reversed_num = 0
while num != 0:
    digit = num % 10
    reversed_num = reversed_num * 10 + digit
    num = num // 10
print ("The reverse of given number is :",reversed_num)