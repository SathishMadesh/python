#print an list of odd numbers till the user's given number

num = int(input("Enter the last number of a list: "))
list = []
for i in range(1,num):
    if i%2 != 0:
        list.append(i)
    
print(list)
