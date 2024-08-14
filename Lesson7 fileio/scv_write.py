import csv

name = input("What is your name? ")
grade = input("What is your grade? ")

with open("names2.csv","a")  as file:
#    writer = csv.writer(file)
#    writer.writerow([name, grade])
    writer = csv.DictWriter(file, fieldnames=["name","grade"],lineterminator="")
    writer.writerow({"name": name, "grade": grade})