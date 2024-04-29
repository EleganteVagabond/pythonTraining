from .student_demo import Student

file_name = "data.txt"
students = []
with open(file_name) as f :
    for line in f :
        students.append(Student.decode(line.strip()))

print(students)
rec_to_add="jo,schmo:python,ruby,javascript"
