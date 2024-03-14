import os
import zipfile
from input import get_student_info, get_course_info, get_marks_info


def compress_files(output_filename, *filenames):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file in filenames:
            zipf.write(file)
            os.remove(file)  

def decompress_files(input_filename):
    with zipfile.ZipFile(input_filename, 'r') as zipf:
        zipf.extractall()

def write_to_file(filename, data):
    with open(filename, 'w') as f:
        for item in data:
            f.write(','.join(item) + '\n')

def read_from_file(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            data.append(tuple(line.strip().split(',')))
    return data

def main():
    if os.path.exists('students.dat'):
        decompress_files('students.dat')
        students = read_from_file('students.txt')
        courses = read_from_file('courses.txt')
        marks = read_from_file('marks.txt')
    else:
        _extracted_from_main_10()

def _extracted_from_main_10():
    students = get_student_info()
    courses = get_course_info()
    marks = get_marks_info(students, courses)

    write_to_file('students.txt', students)
    write_to_file('courses.txt', courses)
    write_to_file('marks.txt', marks)

    compress_files('students.dat', 'students.txt', 'courses.txt', 'marks.txt')

if __name__ == "__main__":
    main()