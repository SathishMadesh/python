#Print the string in right angled triangle pattern

s = input("Enter a string : ")

for i in range (len(s)+1):
    for j in range (i):
        print (s[j],end=" ")
    print()