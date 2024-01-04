def input_student_info():
    name = input("Enter student name: ")
    student_id = input("Enter student id: ")
    dob = input("Enter student dob (YYYY-MM-DD): ")  # Assuming DOB is a string for simplicity
    return {'Name': name, 'Id': student_id, 'DOB': dob}


def list_student():
    print("List of Students:")
    for student in studentArray:
        print(student)


def input_course_info():
    course_name = input("Enter course name: ")
    course_id = int(input("Enter course id: "))
    return {'Course Name': course_name, 'Course Id': course_id, 'Student Mark': [0] * numberOfStudents}


def list_course():
    print("List of Courses:")
    for course in CourseArray:
        print(course)


#Select a course, input marks for students in this course
def input_mark():
    course_id = int(input("Enter course id: "))
    for i in range(numberOfStudents):
        mark = float(input("Enter mark for student " + studentArray[i]['Name'] + ": "))
        CourseArray[course_id - 1]['Student Mark'][i] = mark


def list_mark():
    print("List of Marks:")
    for course in CourseArray:
        print(course['Course Name'] + ": " + str(course['Student Mark']))


#MAIN
numberOfStudents = int(input("Enter the number of students: "))
studentArray = []
for i in range(numberOfStudents):
    studentArray.append(input_student_info())

numberOfCourses = int(input("Enter the number of courses: "))
CourseArray = []
for i in range(numberOfCourses):
    CourseArray.append(input_course_info())

list_student()
list_course()

input_mark()
list_mark()

input_mark()
list_mark()