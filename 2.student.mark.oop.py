class Person:
    def input(self):
        self.name = input("Name: ")
        self.id = input("Id: ")
        return self


class Student(Person):
    def __init__(self):
        super().input()
        self.dob = input("Dob(DD/MM/YYYY): ")

    def __repr__(self):
        return str(self.__dict__)


class Course:
    def __init__(self, num_students):
        self.input()
        self.marks = ['0'] * num_students

    def input(self):
        self.name = input("Course name: ")
        self.id = input("Course id: ")
        return self

    def input_marks(self, students):
        print(f"Enter marks for {self.name}")
        for i, student in enumerate(students):
            self.marks[i] = float(input(f"Student {student.name}: "))

    def __repr__(self):
        return str(self.__dict__)


class School:
    def __init__(self):
        self.students = []
        self.courses = []

    def add_entities(self, num, entity_type):
        for _ in range(num):
            if entity_type == "student":
                self.students.append(Student())
            elif entity_type == "course":
                self.courses.append(Course(len(self.students)))

    def input_course_marks(self):
        for course in self.courses:
            course.input_marks(self.students)

    def list(self, entity_type):
        if entity_type == "student":
            print("List Students:")
            for student in self.students:
                print(student)
        elif entity_type == "course":
            print("List Courses:")
            for course in self.courses:
                print(course)


school = School()
num_students = int(input("The number of students: "))
while num_students >= 50:
    print("Number of students exceeds the limit. Re-enter the number of students less than or equal to 50: ")
    num_students = int(input("Number of students (Remember, less than or equal to 50): "))
school.add_entities(num_students, "student")
num_courses = int(input("The number of courses: "))
school.add_entities(num_courses, "course")
school.input_course_marks()
school.list("student")
school.list("course")