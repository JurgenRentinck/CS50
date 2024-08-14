class Wizard:
    def __init__(self,name):
        if not name:
            raise ValueError("Missing name")
        self.name = name
    
    ...


class Student(Wizard):
    def __init__(self,name,grade):
        super().__init__(name)
        self.house = grade

    ...


class Professor(Wizard):
    def __init__(self,name,subject):
        super().__init__(name)
        self.subject = subject

    ...

wizard = Wizard("Arie")
student = Student("Jurgen", "A")
professor = Professor("Tinus", "Nederlands")