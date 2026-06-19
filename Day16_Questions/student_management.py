# Question:
# Create a Student class with attributes:
# roll_no, name, marks
#
# Accept details of 3 students.
# Display student details.
# Find the student with highest marks.
#
# Topic:
# Class, Object, Constructor, List

class Student:

    def __init__(self, roll_no, name, marks):
        self.roll_no = roll_no
        self.name = name
        self.marks = marks

    def display(self):
        print("Roll No:", self.roll_no)
        print("Name:", self.name)
        print("Marks:", self.marks)
        print()

students = []

for i in range(3):
    roll_no = int(input("Enter Roll No: "))
    name = input("Enter Name: ")
    marks = int(input("Enter Marks: "))

    s = Student(roll_no, name, marks)
    students.append(s)

print("\nStudent Details")

for student in students:
    student.display()

topper = students[0]

for student in students:
    if student.marks > topper.marks:
        topper = student

print("Topper:", topper.name)
print("Marks:", topper.marks)