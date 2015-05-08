
import json
import os
import csv

os.chdir('C:\\Users\\nikita\\Documents\\6339Project\\Project')


bus_id=[]
typ = []
nam = []
neigh = []
fu_add = []
cit = []
stat = []
lat = []
lon = []
star = []
rev_cnt = []
cat = [] 

                       
with open('yelp_academic_dataset_business.json') as f2:
    
    f1 = open("business.csv",'wt', newline='', encoding='utf-8')
    writer = csv.DictWriter(f1, fieldnames = ["Business_ID","Type","Name","Full_Address","City","State","Lattitude","Longitude","Star","Review_Count","Neighbour","Category"], delimiter = ',')
    writer.writeheader()

    wr = csv.writer(f1, dialect='excel')

    for line in f2:
        dict_line = json.loads(line)
        bus_id.append(dict_line['business_id'])
        typ.append(dict_line['type'])
        nam.append(dict_line['name'])
        fu_add.append(dict_line['full_address'])
        cit.append(dict_line['city'])
        stat.append(dict_line['state'])
        lat.append(dict_line['latitude'])
        lon.append(dict_line['longitude'])
        star.append(dict_line['stars'])
        rev_cnt.append(dict_line['review_count'])
        str1 =  dict_line['neighborhoods']
        str2 = ','.join(map(str,str1))
        neigh.append(str2)
        str3 =  dict_line['categories']
        str4 = ','.join(map(str,str3)) 
        cat.append(str4)
    rows = zip(bus_id,typ,nam,fu_add,cit,stat,lat,lon,star,rev_cnt,neigh,cat)
    for row  in rows:
        wr.writerow(row)
         
    f1.close()          
f2.close()        


