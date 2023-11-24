
import re

file_1 = open('data.txt','r')
read_line = file_1.read()

email_pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?"
phone_pattern = '[7-9][0-9]{9}'

emails = re.findall(email_pattern,read_line)
phones = re.findall(phone_pattern,read_line)

file_2 = open('valid.txt','w')

for email in emails:
    print(email, file = file_2)
for phone in phones:
    print(phone, file = file_2)

file_2.close()
file_1.close()

