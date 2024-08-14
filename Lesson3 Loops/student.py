def main():
    #List
    students = ["Piet","Harry","Ron"]

    for student in students:
        print(student)

def main2():
    #List
    students = ["Piet","Harry","Ron"]

    for i in range(len(students)):
        print(i + 1, students[i])

def main3():
    #dictionary
    students = {
        "Piet":"A",
        "Harry":"B",
        "Ron":"E"
    }

    #print(students["Piet"])

    for student in students:
        print(student, students[student], sep=",")

def main4():
    #list with dictionaries
    students = [
        {"name":"Piet","grade":"A","lesson":"English"},
        {"name":"Harry","grade":"B","lesson":"Dutch"},
        {"name":"Ron","grade":"E","lesson":"Math"},
        {"name":"Arie","grade":"D","lesson":None}
    ]

    for student in students:
        print(student["name"],"has a", student["grade"],
              "for",student["lesson"])
    

main()
main2()
main3()
main4()