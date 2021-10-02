import csv
import os
header=['Name of Book','Author','Language','Online Available']
data=[{'Name of Book':'Let us C','Author':'Yash Kanetkar','Language':'C','Online Available':'true https://1lib.in/book/496186/f64010'},
{'Name of Book':'Learn Python 3 the hard way','Author':'Zed A. Shaw','Language':'Python 3','Online Available':'true https://1lib.in/book/3492905/ebdb92'},
{'Name of Book':'Artificial Intelligence Engines: A Tutorial Introduction to the Mathematics of Deep Learning','Author':'James Stone','Language':'English','Online Available':'true https://1lib.in/book/11703684/d5303a'}
]
save_path = os.getcwd()+'\codes\csvReaderWriter\data'
file_name = "data.csv"
csv_file = os.path.join(save_path, file_name)
print(csv_file)
try:
    with open(csv_file,'w') as csvfile:
        writer=csv.DictWriter(csvfile,fieldnames=header)
        writer.writeheader()
        for row in data:
            writer.writerow(row)
except IOError:
    print('i/o error')
print('Finished')