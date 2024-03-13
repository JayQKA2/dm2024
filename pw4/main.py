from domains.school import School
import input
import output

def main():
    school = School()


    num_students = input.get_number_input("Enter number of students: ", max_value=50)
    for _ in range(num_students):
        name, id, dob = input.get_student_info()
        school.add_student(name, id, dob)

    num_courses = input.get_number_input("Enter number of courses: ")
    for _ in range(num_courses):
        name, id, credits = input.get_course_info()
        school.add_course(name, id, credits)

    school.input_course_marks(input.get_mark_input)
    
    print("\n--- Students List ---")
    school.list_students(output.list_students)
    
    print("\n--- Courses List ---")
    school.list_courses(output.list_courses)

if __name__ == "__main__":
    main()