
def get_number_input(prompt, max_value=None, is_float=False):
    while True:
        try:
            num = float(input(prompt)) if is_float else int(input(prompt))
            if max_value is not None and num > max_value:
                print(f"Number exceeds the limit. Please re-enter a number less than or equal to {max_value}.")
            else:
                return num
        except ValueError:
            print("Use numbers please.")

def get_student_info():
    students = []
    num = get_number_input("Enter the number of students: ", is_float=False)
    while num > 50:
        print("Number of students exceeds the limit. Re-enter the number of students less than or equal to 50: ")
        num = get_number_input("Number of students (Remember, less than or equal to 50): ", is_float=False)

    for _ in range(num):
        student_name = input("Name: ")
        student_id = input("ID: ")
        student_dob = input("dob (DD/MM/YYYY): ")
        students.append((student_name, str(student_id), student_dob))
    return students

def get_course_info():
    courses = []
    num_courses = get_number_input("Enter the number of courses: ", is_float=False)

    while num_courses > 10: 
        print("Number of courses exceeds the limit. Please enter a number of courses less than or equal to 10.")
        num_courses = get_number_input("Number of courses : ", is_float=False)
    for _ in range(num_courses):
        course_name = input("Enter course name : ")
        if course_name.lower() == 'done':
            break
        course_id = input("Enter course ID: ")
        course_credits = get_number_input("Enter course credits: ", is_float=True)
        courses.append((course_name, str(course_id), str(course_credits)))
    return courses

def get_marks_info(students, courses):
    marks = []
    for student in students:
        for course in courses:
            mark = get_number_input(f"Enter {student[0]}'s mark for {course[0]}: ", is_float=True)
            if mark == -1:
                continue
            marks.append((student[1], course[1], str(mark)))
    return marks
def write_to_file(filename, data):
    with open(filename, 'w') as file:
        for item in data:
            file.write(','.join(item) + '\n')

def read_from_file(filename):
    data = []
    with open(filename, 'r') as file:
        for line in file:
            data.append(tuple(line.strip().split(',')))
    return data