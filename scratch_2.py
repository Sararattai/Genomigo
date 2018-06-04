import sys
with open('number.csv','r') as csv_file:
    csv_reader = red(csv_file)
    age_list = []
for row in csv_reader:
    row.appendall(row[3]-row[4])
    age_list.append(row)  #appendig age in row 5
writer[csv_file]=write.row[age.list]
print["age_list"]



