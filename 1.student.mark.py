def input_student_info():
    name = input("Student name: ")
    student_id = input("Id: ")
    dob = input("Dob (DD/MM/YYYY): ") 
    return {'Name': name, 'Id': student_id, 'DOB': dob}

def list_student(studentArray):  
    print("List Students:")
    for student in studentArray:
        print(student)
        
def input_course_info():
    course_name = input("Course name: ")
    course_id = int(input("Course id: "))
    return {'Course Name': course_name, 'Course Id': course_id, 'Student Mark': [0] * numberOfStudents}

def list_course(CourseArray):  
    print("List Courses:")
    for course in CourseArray:
        print(course)

def input_mark():
    for _ in range(numberOfCourses):
        course_id = int(input("Course id to input marks: "))
        course = next((c for c in CourseArray if c['Course Id'] == course_id), None)
        if course is not None:
            print(f"Enter marks for {course['Course Name']} :")
            scores = []
            for student in studentArray:
                mark = float(input(f"Student {student['Name']}: "))
                scores.append(mark)
            course['Student Mark'] = scores
        else:
            print("Wrong course ID !!!")

def list_mark():
    print("List Marks:")
    for course in CourseArray:
        print(course['Course Name'] + ": " + str(course['Student Mark']))

numberOfStudents = int(input("The number of students: "))
while numberOfStudents >= 50:
    print("Number of students exceeds the limit. you should do something with the extra students and re-enter the number of students here:")
    numberOfStudents = int(input("Number of students (Remember, less than or equal to 50): "))

studentArray = []
for i in range(numberOfStudents):
    studentArray.append(input_student_info())

numberOfCourses = int(input("The number of courses: "))
CourseArray = []
for i in range(numberOfCourses):
    CourseArray.append(input_course_info())

list_student(studentArray)  
list_course(CourseArray)  

input_mark()
list_mark()

input_mark()
list_mark()