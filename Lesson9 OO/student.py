
def main():
    #student is a tuple, inmutable list
    student = get_student()
    # tuple solution print(f"{student[0]} with grade {student[1]}")
    # dict solution
    print(f"{student["name"]} with grade {student["grade"]}")


#def get_name():
#    return input("name ")

#def get_grade():
#    return input("grade ")

def get_student():
    student = {}
    student["name"] = input("name ")
    student["grade"] = input("grade ")
    return student
    
    
    #name = input("name ")
    #grade = input("grade ")
    #return a tuple
    #return (name,grade)

if __name__ == "__main__":
    main()