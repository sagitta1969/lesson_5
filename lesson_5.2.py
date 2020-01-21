"""
counter = 0
with open('less_5.2.txt', 'r') as f_obj:
    for line in f_obj:
        counter += 1
        line_words = line.split(' ')
        print(line, "длина строки: ", len(line_words))
    print("всего строк", counter)
"""
with open('less_5.2.txt') as f:
    my_line = f.readlines()
    for i, value in enumerate(my_line):
        number_of_words = len(value.split())
        print("строка {} содержит {} слов".format(i + 1, number_of_words))