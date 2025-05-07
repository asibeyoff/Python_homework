# grades managing 
import csv
from collections import defaultdict

# Read grades from the file itself 
grades = defaultdict(list)
with open("grades.csv", newline='') as f:
    reader = csv.DictReader(f)
    for row in reader:
        grades[row['Subject']].append(int(row['Grade']))

# average 
averages = {subject: sum(scores)/len(scores) for subject, scores in grades.items()}

# Write average grades to new CSV
with open("average_grades.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["Subject", "Average Grade"])
    for subject, avg in averages.items():
        writer.writerow([subject, round(avg, 1)])
