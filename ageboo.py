adds_list[len(adds_list)-1]
 fifty_or_ greater = []
for row in add_list:
    name = row[0]
    age = row[1]
    if age >= 50:
        fifty_or_greater.append(name)
        print(fifty_or_greater)
    else:
        print(none)


