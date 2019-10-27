with open("data/unsorted_names.txt") as input_file:
    sorted_names = sorted(input_file)
with open("sorted_names.txt", "w") as output_file:
    for name in sorted_names:
        output_file.write(name)
