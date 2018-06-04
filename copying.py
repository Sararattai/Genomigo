import csv
with open("number.csv",'r') as csv_file:
    csv_reader = csv.Dicreader(csv_file)
    with open('new.csv','w') as new_file:
        fields = ["First name",'last name','address','age']
        csv_writer = csv.Dicwriter[new_file,fields,delimiter = '\t']
        csv_writer.write header()
        for row in csv_reader:
            del row['zipcode']
            csv_writer.write(row)



