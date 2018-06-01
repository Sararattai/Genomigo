import csv
with open("users.csv",'r') as csv_file
csv_reader= csv_reader[csv_file]
max_age = none
for row in csv_file:
  age = int[row['age']]
  max_age = age
  if max_age != none:
    print("%d is the maximum age in the csv file ", max_age)
 
  
