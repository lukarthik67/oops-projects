class Student:
    def __init__(self, name, roll_number, marks):
        self.name = name
        self.roll_number = roll_number
        self.marks = marks

    def display_info(self):
        print(f"{self.name} having roll number-{self.roll_number} obtained marks-{self.marks}.")

student_1 = Student("Karthik", 36, 99)
student_2 = Student("Ram", 50, 100)

student_1.display_info()
student_2.display_info()
