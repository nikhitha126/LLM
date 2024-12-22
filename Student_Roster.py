class Student:
    def __init__(self):
        self.sid= sid
        self.sname = sname
        self.student_class = None
    def display(self):
        print("Original attributes and their values of the Student class:")
        print(f"Student ID: {self.sid}")
        print(f"Student Name: {self.sname}")
        if self.student_class:
            print(f"Student Class: {self.student_class}")
sid = input("Enter Student Id: ")
sname = input("Enter Student Name: ")
student = Student()
student.display()
