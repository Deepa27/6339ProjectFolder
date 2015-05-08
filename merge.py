import csv
from collections import OrderedDict
import sys

csv.field_size_limit(2147483647)
filenames = "BID_STR.csv", "output1.csv"
data = OrderedDict()
fieldnames = []
for filename in filenames:
    with open(filename, "rb") as fp: # python 2
        reader = csv.DictReader(fp)
        fieldnames.extend(reader.fieldnames)
        for row in reader:
            data.setdefault(row["Business_ID"], {}).update(row)

fieldnames = list(OrderedDict.fromkeys(fieldnames))
with open("merged.csv", "wb") as fp:
    writer = csv.writer(fp)
    writer.writerow(fieldnames)
    for row in data.itervalues():
        writer.writerow([row.get(field, '') for field in fieldnames])