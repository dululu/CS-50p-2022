# students = ["Hermione","Harry","Ron"]
# for s in range(len(students)):
#     print(s+1,students[s])

# students = {"Hermione":"a","Harry":"b","Ron":"c"}
# for s in students:
#     print(s,students[s],sep=", ")

students = [
    {"name":"Hermione","house":"Gryffindor","pat":"Otter"},
    {"name":"Harry","house":"Gryffindor","pat":None},
]
for student in students:
    print(student["name"],student["house"],student["pat"],sep=", ")