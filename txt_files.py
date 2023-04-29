def sort_file():
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        content = file.readlines()
        content.sort()
    with open(file_name, 'w') as file:
        file.writelines(content)

sort_file()

