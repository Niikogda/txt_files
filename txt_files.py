def check_duplicates():
    file_name = input("Enter file name: ")
    with open(file_name, 'r') as file:
        content = file.readlines()
        unique_content = set(content)
        if len(content) == len(unique_content):
            print("No duplicate lines found in the file")
        else:
            print("Duplicate lines found in the file")

check_duplicates()

