def get_number_input(prompt, max_value=None, is_float=False):
    while True:
        try:
            num = float(input(prompt)) if is_float else int(input(prompt))
            if max_value is not None and num > max_value:
                print(f"Number exceeds the limit. Please re-enter a number less than or equal to {max_value}: ")
            else:
                return num
        except ValueError:
            print("Use numbers please: ")

def get_student_info():
    name = input("Name: ")
    id = input("Id: ")
    dob = input("Dob(DD/MM/YYYY): ")
    return name, id, dob

def get_course_info():
    name = input("Course name: ")
    id = input("Course id: ")
    credits = get_number_input(f"Credit for {name}: ")
    return name, id, credits

def get_mark_input(student_name, course_name):
    return get_number_input(f"Enter marks for {student_name} in {course_name}: ", is_float=True)