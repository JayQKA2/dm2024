import math
import numpy as np

class Person:
    def __init__(self, name, id, dob):
        self.name = name
        self.id = id
        self.dob = dob

    def __repr__(self):
        return str(self.__dict__)

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
        return round(average_gpa, 1)

    def __repr__(self):
        marks_str = ", ".join([f"{course}: {mark}" for course, mark in self.marks.items()])
        return f"Name: {self.name}, ID: {self.id}, DOB: {self.dob}, Marks: {marks_str}, GPA: {self.calculate_gpa()}"

class Course:
    def __init__(self, name, id, credits):
        self.name = name
        self.id = id
        self.credits = credits

    def __repr__(self):
        return str(self.__dict__)

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_entities(self, num, entity_type):
        while num > 50:
            print("Number of students exceeds the limit. Re-enter the number of students less than or equal to 50: ")
            num = int(input("Number of students (Remember, less than or equal to 50): "))
        for _ in range(num):
            if entity_type == "student":
                name = input("Name: ")
                id = input("Id: ")
                dob = input("Dob(DD/MM/YYYY): ")
                self.students.append(Student(name, id, dob))
            elif entity_type == "course":
                name = input("Course name: ")
                id = input("Course id: ")
                credits = int(input(f"Credit for {name}: "))
                self.courses.append(Course(name, id, credits))

    def input_course_marks(self):
        for course in self.courses:
            for student in self.students:
                mark = float(input(f"Enter marks for {student.name} in {course.name}: "))
                student.input_mark(course.name, mark)

    def list(self, entity_type):
        if entity_type == "student":
            print("List Students:")
            for student in sorted(self.students, key=lambda s: s.calculate_gpa(), reverse=True):
                print(student)
        elif entity_type == "course":
            print("List Courses:")
            for course in self.courses:
                print(course)


school = School()

num_students = int(input("Enter number of students: "))
school.add_entities(num_students, "student")

num_courses = int(input("Enter number of courses: "))
school.add_entities(num_courses, "course")

school.input_course_marks()

school.list("student")
school.list("course")
