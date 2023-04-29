import re

with open('file.txt', 'r') as file:
    content = file.read()
    numbers = re.findall(r'\d+', content)
    for num in numbers:
        print(num)

