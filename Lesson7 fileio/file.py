


name  = input("What is your name?")

#file = open("names.txt","a")
#file.write(f"{name}\n")
#file.close()

with open("names.txt", "a") as file:
    file.write(f"{name}\n")



#with open("names.txt","r") as file:
#    lines = file.readlines()

#for line in lines:
    #print(f"Hello, {line}", end="")
#    print(f"Hello, {line.rstrip()}")

#with open("names.txt", "r") as file:
#    for line in sorted(file):
#        print(f"Hello, {line.rstrip()}")

#read the file and sort the names alternatief 
# when you want to do something with this
names = []
with open("names.txt","r") as file:
    for line in file:
        names.append(line.rstrip())

for line in sorted(names):
    print(f"Hello, {line.rstrip()}")

#names=[]

#for _ in range(3):
#    name  = input("What is your name?")
#    names.append(name)

#for name in sorted(names):
#        print(f"Hello, {name}")

