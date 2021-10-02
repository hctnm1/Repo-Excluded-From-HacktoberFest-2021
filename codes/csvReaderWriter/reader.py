import csv
import os
save_path = os.getcwd()+'\codes\csvReaderWriter\data'
file_name = "data.csv"
csv_file = os.path.join(save_path, file_name)
data=csv.DictReader(open(csv_file,encoding='utf-8-sig'))
read=[]
for row in data:
    read.append(row)
print(read)