# it will accept the input as a string
values = input("Enter the multiple values :").split()
print("The values are:",values)

# it will accept the input as only intigers
values = input("Enter the multiple values :").split()
values = [int(val) for val in values]
print ("The values are :", values)

