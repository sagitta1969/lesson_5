while True:
    line = input("введите строку: ").split()
    if not line:
        break
    with open('text.txt', 'a') as my_file:
        #my_file.write(line[i] + '\n')
        for i in range (len(line)):
            print(line[i], file=my_file)