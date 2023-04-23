with open('count.txt', 'r') as file:
    data = file.read().replace('\n', ' ')
    word_count = len(data.split())
    print("Кількість слів у файлі: ", word_count)
