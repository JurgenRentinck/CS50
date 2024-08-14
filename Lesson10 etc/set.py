students = [
    {"name":"Jurgen","grade":"A"},
    {"name":"Sis","grade":"C"},
    {"name":"thomas","grade":"B"},
    {"name":"Essie","grade":"D"},
]

#grades = []
#for student in students:
#    if student["grade"] not in grades:
#        grades.append(student["grade"])
#
#for grade in sorted(grades):
#    print(grade)

grades = set()
for student in students:
    grades.add(student["grade"])

for grade in sorted(grades):
    print(grade)