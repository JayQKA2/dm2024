from .person import Person
from math import ceil

class Student(Person):
    def __init__(self, name, id, dob):
        super().__init__(name, id, dob)
        self.marks = {}

    def input_mark(self, course_name, mark):
        self.marks[course_name] = mark

    def get_marks(self):
        return self.marks

    def calculate_gpa(self):
        total_marks = sum(self.marks.values())
        num_of_courses = len(self.marks)
        average_gpa = total_marks / num_of_courses
        return ceil(average_gpa * 10) / 10 

    def __repr__(self):
        marks_str = ", ".join([f"{course}: {mark}" for course, mark in self.marks.items()])
        return f"Name: {self.name}, ID: {self.id}, DOB: {self.dob}, Marks: {marks_str}, GPA: {self.calculate_gpa()}"