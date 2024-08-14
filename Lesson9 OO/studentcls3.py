######Class definition
class Student:    

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return (f"{self.name} with grade {self.grade}")

    @classmethod
    def get(cls):
        name = input("Name: ")
        grade = input("Grade ")
        return cls(name,grade)




######Mainline
def main():
    student = Student.get()
    print(student)
 


if __name__ == "__main__":
    main()