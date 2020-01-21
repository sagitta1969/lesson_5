from random import randint

el_sum = 0
with open('less_5.5.txt', 'w') as m_file:
    for i in range(50):
        el = randint(1, 30)
        el_sum += el
        m_file.write(str(el) + ' ')

print("сумма элементов: " + str(el_sum))