import csv

students = []

#with open("names.csv","r") as file:
#    reader = csv.reader(file)
 #   for row in reader:
 #       students.append({"name": row[0], "grade" : row[1], "lesson" : row[2]})
 # 

with open("names.csv","r") as file:
    #use DictReader to return dicts, but add column name in csv file
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "grade" : row["grade"], "lesson" : row["lesson"]})

for student in sorted(students, key=lambda student: student["name"]):        
    print(f"{student["name"]} has a {student["grade"]}")