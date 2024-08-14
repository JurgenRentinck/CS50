students = [
    {"name": "Piet", "grade": "A", "lesson": "English"},
    {"name": "Harry", "grade": "B", "lesson": "Dutch"},
    {"name": "Ron", "grade": "B", "lesson": "Math"},
    {"name": "Arie", "grade": "D", "lesson": None},
]


bees = [student["name"] for student in students if student["grade"] == "B"]

for bee in sorted(bees):
    print(bee)
