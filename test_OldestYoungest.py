import csv
import unittest
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

class TestFindOldestAndYoungest(unittest.TestCase):
    
    def setUp(self):
        self.csv_data = """First Name,Last Name,Date of birth
Oskar,Grimminger,2005-10-29
Konrad,Grimminger,2007-08-20
Max,Grimminger,1974-07-8
"""
        
        self.filename = 'test_people.csv'
        with open(self.filename, mode ='w') as file:
            file.write(self.csv_data)

    def test_find_oldest_and_youngest(self):
        oldest, youngest = find_oldest_and_youngest(self.filename)
        self.assertEqual(oldest, "Max Grimminger")
        self.assertEqual(youngest, "Konrad Grimminger")

    def tearDown(self):
        import os
        os.remove(self.filename)

if __name__ == '__main__':
    unittest.main()




