import csv
fp=open('data.csv','w',newline="")
csv_obj = csv.writer(fp)
csv_obj.writerow(["Writing into csv file"])
fp.close