import csv
from datetime import datetime

def find_oldest_and_youngest(filename):
    with open(filename, mode='r') as file:
        csv_reader = csv.DictReader(file)
        oldest_person = None
        youngest_person = None
        oldest_date = None
        youngest_date = None

        for row in csv_reader:
            dob = datetime.strptime(row['Date of birth'], '%Y-%m-%d')  
            if oldest_date is None or dob < oldest_date:
                oldest_date = dob
                oldest_person = row['First Name'] + ' ' + row['Last Name']
            if youngest_date is None or dob > youngest_date:
                youngest_date = dob
                youngest_person = row['First Name'] + ' ' + row['Last Name']

        return oldest_person, youngest_person


filename = '100_people.csv'  
oldest, youngest = find_oldest_and_youngest(filename)
print(f"Osldest Person: {oldest}")
print(f"Youngest Person: {youngest}")


