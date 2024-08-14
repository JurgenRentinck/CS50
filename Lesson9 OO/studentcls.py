class Student:
    def __init__(self, name, grade, lesson ):
        if not name:
            raise ValueError("Missing name.")
        if grade not in ["A","B","C","D"]:
            raise ValueError("Invalid grade.")
        self.name = name
        self.grade = grade
        self.lesson = lesson

    def __str__(self):
        return (f"{self.name} with grade {self.grade}")

    def getLesson(self):
        match self.lesson:
            case "math":
                return "m"
            case "dutch":
                return "d"
            case _:
                return "unkown"
       

def main():
    student = get_student()
    print(student)
    print(student.getLesson())

def get_student():

    name = input("name ?")
    grade = input("Grade ?")
    lesson = input("Lesson ?")
    return Student(name,grade, lesson)


if __name__ == "__main__":
    main()