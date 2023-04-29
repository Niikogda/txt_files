def print_last_n_lines():
    file_name = input("Enter file name: ")
    n = int(input("Enter number of lines to print: "))
    with open(file_name, 'r') as file:
        stack = []
        for line in file:
            stack.append(line.strip())
            if len(stack) > n:
                stack.pop(0)
        for line in stack:
            print(line)

print_last_n_lines()

