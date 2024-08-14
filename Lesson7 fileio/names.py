
#CSV files

#with open("names.csv","r") as file:
#    for line in sorted(file):
#        #row = line.rstrip().split(",")
#        #print(f"{row[0]} has a {row[1]}")
#        name,grade = line.rstrip().split(",")
#        print(f"{name} has a {grade}")


students = []
with open("names.csv","r") as file:
    for line in file:
        name,grade,lesson = line.rstrip().split(",")
        #student = {}
        #student["name"] = name
        #student["grade"] = grade
        student = {"name": name, "grade" : grade, "lesson" : lesson}
        students.append(student)

#function used to sort the dictionary, 
# better to used lambda function or annonimous function
#def get_name(student):
#    #return student["grade"]
#    return student["name"]

#for student in sorted(students, key=get_name):        
#shorter with lambda function
for student in sorted(students, key=lambda student: student["name"]):        
    print(f"{student["name"]} has a {student["grade"]}")
