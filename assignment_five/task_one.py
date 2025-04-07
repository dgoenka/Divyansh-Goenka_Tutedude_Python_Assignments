marks = {"Alice": 100}
name = input("Enter the student's name: ")
try:
    print(name + "'s marks: " + str(marks[name]))
except KeyError:
    print("Student not found")
