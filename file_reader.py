filename = '100_people.csv'

with open(filename) as file_object:
    for line in file_object:
        print(line.rstrip())

