# Create a class Student with:
# ●	A constructor that accepts name, roll number, and marks.
# ●	A method display_details() that prints all details.
# ●	A method check_result() that returns "Pass" if marks are at least 40, otherwise "Fail".
# Create three objects and display their results.

class Student:

    def __init__(self,name,roll_number,marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_details(self):
        print(f"\nName: {self.name}\nRoll Number : {self.roll_number}\nMarks: {self.marks}")


    def check_result(self):
        if self.marks >= 40:
            return "Pass"
        return "Fail"


student1 = Student("Albert", 745848498, 50)
student1.display_details()
print(student1.check_result())

student2 = Student("Barbara", 838495645, 40)
student2.display_details()
print(student2.check_result())

student3 = Student("Charlie", 746327, 39.99)
student3.display_details()
print(student3.check_result())