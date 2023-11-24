import re

file_1 = open('data.txt','r')

email_pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
phone_pattern = '[7-9][0-9]{9}'

file_2 = open('valid.txt','w')

for line in file_1:
    for words in line.split():
        email = re.search(email_pattern,words)
        phone = re.search(phone_pattern,words)
        if email :
            emails = email.group()
            file_2.write(emails + '\n')
        elif phone:
            phones = phone.group()  
            file_2.write(phones + '\n')
           
file_2.close()
file_1.close()