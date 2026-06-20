# Question:
# Add students, display students and find topper.

class Student:

    def __init__(self, roll, name, marks):
        self.roll = roll
        self.name = name
        self.marks = marks

    def display(self):
        print(self.roll, self.name, self.marks)

students = []

n = int(input("Enter number of students: "))

for i in range(n):
    roll = int(input("Roll No: "))
    name = input("Name: ")
    marks = float(input("Marks: "))

    students.append(Student(roll, name, marks))

print("\nStudent Details")
for s in students:
    s.display()

topper = students[0]

for s in students:
    if s.marks > topper.marks:
        topper = s

print("\nTopper:", topper.name)
print("Marks:", topper.marks)