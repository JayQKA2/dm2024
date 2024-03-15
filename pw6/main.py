import os
import zipfile
import pickle
from input import get_student_info, get_course_info, get_marks_info

def compress_files(output_filename, *file_paths):
    with zipfile.ZipFile(output_filename, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for file_path in file_paths:
            zipf.write(file_path)
            os.remove(file_path)

def decompress_files(input_filename):
    with zipfile.ZipFile(input_filename, 'r') as zipf:
        zipf.extractall()

def pickle_data(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def unpickle_data(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def main():
    if os.path.exists('students.pkl.zip'):
        decompress_files('students.pkl.zip')
        students = unpickle_data('students.pkl')
        courses = unpickle_data('courses.pkl')
        marks = unpickle_data('marks.pkl')
    else:
        students = get_student_info()
        courses = get_course_info()
        marks = get_marks_info(students, courses)

        pickle_data('students.pkl', students)
        pickle_data('courses.pkl', courses)
        pickle_data('marks.pkl', marks)

        compress_files('students.pkl.zip', 'students.pkl', 'courses.pkl', 'marks.pkl')

if __name__ == "__main__":
    main()