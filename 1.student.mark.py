def input_student_info():
    name = input("Student name: ")
    student_id = input("Id: ")
    dob = input("Dob (DD/MM/YYYY): ") 
    return {'Name': name, 'Id': student_id, 'DOB': dob}

def list_student():
    print("List Students:")
    for student in studentArray:
        print(student)

def input_course_info():
    course_name = input("Course name: ")
    course_id = int(input("Course id: "))
    return {'Course Name': course_name, 'Course Id': course_id, 'Student Mark': [0] * numberOfStudents}

def list_course():
    print("List Courses:")
    for course in CourseArray:
        print(course)

def input_mark():
    course_id = int(input("Course id: "))
    if 1 <= course_id <= numberOfCourses:
        for i in range(numberOfStudents):
            mark = float(input("Enter mark for student " + studentArray[i]['Name'] + ": "))
            CourseArray[course_id - 1]['Student Mark'][i] = mark

def list_mark():
    print("List Marks:")
    for course in CourseArray:
        print(course['Course Name'] + ": " + str(course['Student Mark']))

numberOfStudents = int(input("The number of students: "))
while numberOfStudents >= 100:
    print("Number of students exceeds the limit. you should do something with the extra students and re-enter the number of students here:")
    numberOfStudents = int(input("Number of students (remember, less than 100): "))

studentArray = []
for i in range(numberOfStudents):
    studentArray.append(input_student_info())

numberOfCourses = int(input("The number of courses: "))
CourseArray = []
for i in range(numberOfCourses):
    CourseArray.append(input_course_info())

list_student()
list_course()

input_mark()
list_mark()

input_mark()
list_mark()
