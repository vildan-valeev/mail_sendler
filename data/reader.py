import csv
outfile = 'csv_file.csv'
from itertools import islice

data_reader = csv.reader(open(outfile))
batch_size = 1000
while True:
    batch = [row for row in islice(data_reader, batch_size)]
    if not batch:
        break
    print(batch)



# import csv
# outfile = 'csv_file.csv'
# with open(outfile, 'w') as f:
#     rows = csv.reader(f)
#     print(rows)
#     for i in rows:
#         print(i[0])
