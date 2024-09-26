import csv
import random

lead_team = ["CEO", "Lead1", "Lead2", "Lead3", "Lead4"]
weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
persons = []

with open('office.csv') as csvfile:
    reader = csv.reader(csvfile)
    next(reader) 
    for col in reader:
        person = col[0]
        department = col[1]
        persons.append((person, department))

for lead in lead_team:
    persons.append((lead, "Lead"))

daily_assignments = {day: [] for day in weekdays}

def assign_person_to_days(person, days_count=3):
    assigned_days = random.sample(weekdays, days_count)
    for day in assigned_days:
        daily_assignments[day].append(person)

for person in persons:
    if person[0] not in lead_team:
        assign_person_to_days(person)
    else:
        for day in weekdays:
            daily_assignments[day].append(person)

for day in weekdays:
    non_lead_persons = [p for p in persons if p[0] not in lead_team]
    while len(daily_assignments[day]) < 15 + len(lead_team):
        remaining_persons = [p for p in non_lead_persons if p not in daily_assignments[day]]
        if remaining_persons:
            daily_assignments[day].append(random.choice(remaining_persons))

for day in weekdays:
    print(f"\n--- {day} ---")
    for assignment in daily_assignments[day]:
        print(f"Person: {assignment[0]}, Department: {assignment[1]}")











