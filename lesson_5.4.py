r_dic = {'one': 'один', 'two': 'два', 'three': 'три', 'four': 'четыре'}

with open('less_5.44.txt', 'a') as n_file:
    with open('less_5.4.txt') as my_file:
        line = my_file.read().split('\n')
        for i in line:
            i = i.split(' ')
            n_file.writelines(r_dic[i[0]] + ' - ' + i[1] + '\n')