"""
Задача 38: Дополнить телефонный справочник возможностью изменения
и удаления данных. Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных.

"""


from csv import DictWriter, DictReader
from os.path import exists

def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()

def get_info():
    mas_info = ['Иванов', 'Иван', 123]
    return mas_info

def write_file(lst):
    with open('phone.csv', 'r', encoding='utf-8',) as f_n:
        f_n_reader = DictReader(f_n)
        res = list(f_n_reader)
    with open('phone.csv', 'w', encoding='utf-8', newline='') as f_n:
        obj = {'Фамилия': lst[0], 'Имя': lst[1], 'Номер': lst[2]}
        res.append(obj)
        f_n_writer = DictWriter(f_n, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_n_writer.writeheader()
        f_n_writer.writerows(res)


def read_file(file_name):
    with open(file_name, encoding='utf-8') as data:
        f_reader = DictReader(data)
        res = list(f_reader)
    return res

def main():
    while True:
        command = input('Введите команду: ')
        if command == 'q':
            break
        elif command == 'r':
            if not exists('phone.csv'):
                create_file()
            print(read_file('phone.csv'))
        elif command == 'w':
            if not exists('phone.csv'):
                create_file()
            write_file(get_info())


main()

