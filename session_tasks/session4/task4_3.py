def get_top_performers(file_path, number_of_top_students = 5):
    with open(file_path) as input_file:
        students = [tuple(line.strip().split(",")) for line in input_file][1:]
    top_students = sorted(students, key = lambda x : float(x[2]), reverse = True)
    return [student[0] for student in top_students[:number_of_top_students]]

def write_students(src_file_path, dest_file_path):
    with open(src_file_path) as input_file:
        top_line = input_file.readline()
        students = [tuple(line.strip().split(",")) for line in input_file]
    sorted_by_age_students = sorted(students, key = lambda x : int(x[1]), reverse = True)
    with open(dest_file_path, "w") as output_file:
        output_file.write(top_line)
        for student in sorted_by_age_students:
            output_file.write(",".join(student) + "\n")


print(get_top_performers("data/students.csv"))
write_students("data/students.csv", "students_output.csv")
