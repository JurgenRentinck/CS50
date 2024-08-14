#dict comprehensions
students = [
    "Piet",
    "Harry",
    "Ron",
    "Arie"
]


sukkels = [{"name":student, "grade":"A"} for student in students]

dictsukkels = {stud: "B" for stud in students}


print(sukkels)
print(dictsukkels)



