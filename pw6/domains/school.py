from .student import Student
from .course import Course

class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_student(self, name, id, dob):
        self.students.append(Student(name, id, dob))

    def add_course(self, name, id, credits):
        self.courses.append(Course(name, id, credits))

    def input_course_marks(self, mark_input_func):
        for course in self.courses:
            for student in self.students:
                mark = mark_input_func(student.name, course.name)
                student.input_mark(course.name, mark)

    def list_students(self, output_func):
        sorted_students = sorted(self.students, key=lambda s: s.calculate_gpa(), reverse=True)
        output_func(sorted_students)

    def list_courses(self, output_func):
        output_func(self.courses)