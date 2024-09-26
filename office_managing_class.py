import csv
import random

class Person:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class TeamAssignment:
    def __init__(self, lead_team, weekdays):
        self.lead_team = [Person(lead, "Lead") for lead in lead_team]
        self.weekdays = weekdays
        self.persons = []
        self.daily_assignments = {day: [] for day in weekdays}

    def load_persons(self, csv_file):
        with open(csv_file) as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for col in reader:
                person = Person(col[0], col[1])
                self.persons.append(person)
        self.persons.extend(self.lead_team)

    def assign_person_to_days(self, person, days_count=3):
        assigned_days = random.sample(self.weekdays, days_count)
        for day in assigned_days:
            self.daily_assignments[day].append(person)

    def distribute_assignments(self):
        for person in self.persons:
            if person not in self.lead_team:
                self.assign_person_to_days(person)
        else:
            for day in self.weekdays:
                self.daily_assignments[day].append(person)

        for day in self.weekdays:
            non_lead_persons = [p for p in self.persons if p not in self.lead_team]
            while len(self.daily_assignments[day]) < 15 + len(self.lead_team):
                remaining_persons = [p for p in non_lead_persons if p not in self.daily_assignments[day]]
                if remaining_persons:
                    self.daily_assignments[day].append(random.choice(remaining_persons))


    def print_assignments(self):
        for day in self.weekdays:
            print(f"\n--- {day} ---")
            for assignment in self.daily_assignments[day]:
                print(f"Person: {assignment.name}, Department: {assignment.department}")

lead_team = ["CEO", "Lead1", "Lead2", "Lead3", "Lead4"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

team_assignment = TeamAssignment(lead_team, weekdays)

team_assignment.load_persons('office.csv')

team_assignment.distribute_assignments()

team_assignment.print_assignments()
