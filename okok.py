import csv
import random

class Person:
    def __init__(self, name, department):
        self.name = name
        self.department = department

class DailyAssignment:
    def __init__(self, weekdays, lead_team):
        self.weekdays = weekdays
        self.lead_team = lead_team
        self.assignments = {day: [] for day in weekdays}

    def assign_lead_team(self):
        for day in self.weekdays:
            self.assignments[day].extend(self.lead_team)

    def assign_person_to_days(self, person, days_count=3):
        assigned_days = random.sample(self.weekdays, days_count)
        for day in assigned_days:
            self.assignments[day].append(person)

    def ensure_minimum_non_leads(self, persons, min_non_leads=15):
        non_lead_persons = [p for p in persons if p not in self.lead_team]
        for day in self.weekdays:
            while len(self.assignments[day]) < min_non_leads + len(self.lead_team):
                remaining_persons = [p for p in non_lead_persons if p not in self.assignments[day]]
                if remaining_persons:
                    self.assignments[day].append(random.choice(remaining_persons))

    def print_assignments(self):
        for day in self.weekdays:
            print(f"\n--- {day} ---")
            for assignment in self.assignments[day]:
                print(f"Person: {assignment.name}, Department: {assignment.department}")

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


    with open('office.csv') as csvfile:
        reader = csv.reader(csvfile)
        next(reader)
        for col in reader:
            person = Person(col[0], col[1])
            persons.append(person)

    assignment = DailyAssignment(weekdays, lead_team)

    assignment.assign_lead_team()

    for person in persons:
        assignment.assign_person_to_days(person)

    assignment.ensure_minimum_non_leads(persons)

    assignment.print_assignments()

if __name__ == "__main__":
    main()
