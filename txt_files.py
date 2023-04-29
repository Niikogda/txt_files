def delete_line():
    file_name = input("Enter file name: ")
    line_to_delete = input("Enter the line to delete: ")
    with open(file_name, 'r') as file:
        content = file.readlines()
    with open(file_name, 'w') as file:
        for line in content:
            if line.strip() != line_to_delete:
                file.write(line)

delete_line()

