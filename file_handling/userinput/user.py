import csv
fp = open('data.csv','w',newline="")

csv_obj = csv.writer(fp)
csv_obj.writerow(['uid','uname','uemail'])
no_users = int(input("Enter the No.of Users : "))

for x in range (no_users):
    uid = int(input("Enter the user id :"))
    uname = input("Enter the user name :")
    uemail = input("Enter the user email :")

    csv_obj.writerow([uid, uname, uemail])

fp.close()