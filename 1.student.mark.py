def input_student_info():
    name = input("Student name: ")
    student_id = input("Id: ")
    dob = input("Dob (DD/MM/YYYY): ") 
    return {'Name': name, 'Id': student_id, 'DOB': dob}

def list_student(student_array):  
    print("List Students:")
    for student in student_array:
        print(student)
        
def input_course_info():
    course_name = input("Course name: ")
    course_id = int(input("Course id: "))
    return {'Course Name': course_name, 'Course Id': course_id, 'Student Mark': [0] * number_of_students}

def list_course(course_array):  
    print("List Courses:")
    for course in course_array:
        print(course)

def input_mark():
    for _ in range(number_of_courses):
        course_id = int(input("Course id to input marks: "))
        course = next((c for c in course_array if c['Course Id'] == course_id), None)
        if course is not None:
            print(f"Enter marks for {course['Course Name']} :")
            scores = []
            for student in student_array:
                mark = float(input(f"Student {student['Name']}: "))
                scores.append(mark)
            course['Student Mark'] = scores
        else:
            print("Wrong course ID !!!")

def list_mark():
    print("List Marks:")
    for course in course_array:
        print(course['Course Name'] + ": " + str(course['Student Mark']))

number_of_students = int(input("The number of students: "))
while number_of_students >= 50:
    print("Number of students exceeds the limit. you should do something with the extra students and re-enter the number of students here:")
    number_of_students = int(input("Number of students (Remember , less than or equal to 50): "))

student_array = []
for i in range(number_of_students):
    student_array.append(input_student_info())

number_of_courses = int(input("The number of courses: "))
course_array = []
for i in range(number_of_courses):
    course_array.append(input_course_info())

list_student(student_array)  
list_course(course_array)  

input_mark()
list_mark()

input_mark()
list_mark()