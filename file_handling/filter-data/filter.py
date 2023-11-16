import json
import csv
fp = open ('data.json',newline="")
data = json.load(fp)
open_csv = open('result.csv','w',newline="")
csv_obj = csv.writer(open_csv)

for item in data:
    if(item['gender'] == 'Male'):
        element = item
        print(element)
        csv_obj.writerow(element)
        
open_csv.close()
fp.close()