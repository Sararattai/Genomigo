import csv
with open = ("number.csv",'r') as csv_file
csv_reader = csv.reader(csv_file)
csv_age = []
for row in csv_reader:
    csv_age.append(row[3])
  print(row[3])
