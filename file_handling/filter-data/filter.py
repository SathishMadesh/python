import json
import csv

try:
    fp = open ('data.json',newline="")
    data = json.load(fp)
    open_csv = open('result.csv','w')
    csv_obj = csv.writer(open_csv)

    for item in data:
        if(item['gender'] == 'Female'):
            print(item)
            csv_obj.writerow([item['id'],item['first_name'],item['email'],item['gender']])

except FileNotFoundError as err:
    print(err)

finally:
    if open_csv:
        open_csv.close()
    if fp :
        fp.close()


