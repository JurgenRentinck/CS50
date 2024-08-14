######Class definition
class Student:    

    def __init__(self, name, grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return (f"{self.name} with grade {self.grade}")

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self,name):
        if not name:
            raise ValueError("Missing name.")
        self._name = name

    #getter, use @property annotation
    # letop, atribuut mag niet dezelfde naam hebben als getter of setter
    # laat attribuut daarom met _ beginnen
    @property
    def grade(self):
        return self._grade
    
    #setter, use the strange annotation
    @grade.setter
    def grade(self,grade):
        if grade not in ["A","B","C","D"]:        
            raise ValueError("Invalid grade.")        
        self._grade = grade


######Mainline
def main():
    student = get_student()
    print(student)
 
def get_student():
    name = input("name ?")
    grade = input("Grade ?")
    return Student(name,grade)

if __name__ == "__main__":
    main()