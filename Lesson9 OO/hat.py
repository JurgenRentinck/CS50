import random

#create a class that is used for classmethods
#for example for a hat that sorts who live in whixh house
#a utility class

class Hat:
    houses = ["Griffindor","Hufflepuff","Ravenclaw","Slytherin"]

    #create class method, convention is not to use self but cls
    @classmethod
    def sort(cls,name):
        house = random.choice(cls.houses)
        print(name, "is in", house)




Hat.sort("Harry")