def replace_line():
    file_name = input("Enter file name: ")
    old_line = input("Enter the line to replace: ")
    new_line = input("Enter the new line: ")
    with open(file_name, 'r+') as file:
        content = file.read()
        file.seek(0)
        new_content = content.replace(old_line, new_line)
        file.write(new_content)

replace_line()

