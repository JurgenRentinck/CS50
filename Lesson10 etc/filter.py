students = [
    {"name":"Piet","grade":"A","lesson":"English"},
    {"name":"Harry","grade":"B","lesson":"Dutch"},
    {"name":"Ron","grade":"B","lesson":"Math"},
    {"name":"Arie","grade":"D","lesson":None}
    ]



def is_bee(s):
    return s["grade"] == "B"


bees = filter(is_bee,students)

for bee in sorted(bees, key=lambda s: s["name"]):
    print(bee["name"])
