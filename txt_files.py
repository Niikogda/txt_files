with open('file.txt', 'r') as file:
    for line in file:
        if 'word' in line:
            print(line.strip())

