import csv
import random
import math

class Person:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class Department:
    def __init__(self, name):
        self.name = name
        self.members = []

    def add_member(self, person):
        self.members.append(person)

    def min_members_per_day(self):
        return math.ceil(len(self.members) / 2)

    def assign_members(self, daily_assignments, weekdays):
        required_members = self.min_members_per_day()

        for day in weekdays:
            available_members = self.members.copy()
            if len(available_members) >= required_members:
                assigned_members = random.sample(available_members, required_members)
            else:
                assigned_members = available_members.copy()

            for member in assigned_members:
                daily_assignments[day].append(member)

class DailyAssignment:
    def __init__(self, weekdays, lead_team):
        self.weekdays = weekdays
        self.lead_team = lead_team
        self.assignments = {day: [] for day in weekdays}

    def assign_lead_team(self):
        for day in self.weekdays:
            self.assignments[day].extend(self.lead_team)

    def print_assignments(self):
        for day in self.weekdays:
            print(f"\n--- {day} ---")
            for assignment in self.assignments[day]:
                print(f"Person: {assignment.name}, Department: {assignment.department}")

    def add_random_person(self, persons):
        for day in self.weekdays:
            random_person = random.choice(persons)
            self.assignments[day].append(random_person)
            print(f"Random hinzugefügte Person am {day}: {random_person.name}, Department: {random_person.department}")

def main():
    lead_team = [
        Person("CEO", "Lead"),
        Person("Lead1", "Lead"),
        Person("Lead2", "Lead"),
        Person("Lead3", "Lead"),
        Person("Lead4", "Lead")
    ]

    weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
    persons = []
    departments = {}

    with open('office.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)  
        for col in reader:
            person = Person(col[0], col[1])
            persons.append(person)

            if col[1] not in departments:
                departments[col[1]] = Department(col[1])

            departments[col[1]].add_member(person)

    assignment = DailyAssignment(weekdays, lead_team)
    
    assignment.assign_lead_team()

    for department in departments.values():
        department.assign_members(assignment.assignments, weekdays)

    assignment.add_random_person(persons)

    assignment.print_assignments()

if __name__ == "__main__":
    main()

    main()

