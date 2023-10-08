"""
Задача 38: Дополнить телефонный справочник возможностью изменения
и удаления данных. Пользователь также может ввести имя или фамилию,
и Вы должны реализовать функционал для изменения и удаления данных.

"""
import csv
from csv import DictWriter, DictReader
from os.path import exists

def create_file():
    with open('phone.csv', 'w', encoding='utf-8', newline='') as data:
        f_writer = DictWriter(data, fieldnames=['Фамилия', 'Имя', 'Номер'])
        f_writer.writeheader()
"""
def get_info():
    mas_info = ['Иванов', 'Иван', 123]
    return mas_info
"""

def get_info():
    info = []
    first_name = input('Введите фамилию: ')
    last_name = input('Введите имя: ')
    info.append(first_name)
    info.append(last_name)
    flag = False
    while not flag:
        try:
            phone_number = int(input('Введите номер телефона: '))
            if len(str(phone_number)) != 11:
                print('wrong number')
            else:
                flag = True

        except ValueError:
            print('not valid number')
        info.append(phone_number)
        return info


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
def change_info(file_name):
    with open(file_name, 'r+', encoding='utf-8') as f:
        f_reader = DictReader(f)
        res = list(f_reader)
        res_enum = list(enumerate(res))
        print(res_enum)

        for i, dict in (res_enum):
            number = int(input('Введите номер контакта для изменения: '))
            if i == number:
                print(i, dict)
                el_1 = input('Введите новую фамилию: ')
                dict['Фамилия'] = el_1
                el_2 = input('Введите новое имя: ')
                dict['Имя'] = el_2
                el_3 = input('Введите новый номер телефона: ')
                dict['Номер'] = el_3

                with open(file_name, 'w', encoding='utf-8', newline='') as f:
                    f_n_writer = DictWriter(f, fieldnames=['Фамилия', 'Имя', 'Номер'])
                    f_n_writer.writeheader()
                    f_n_writer.writerows(res)
                print('Контакт успешно изменен')
                break

def del_info(file_name):
    with open(file_name, 'r+', encoding='utf-8') as f:
        f_reader = DictReader(f)
        res = list(f_reader)
        res_enum = list(enumerate(res))
        print(res_enum)
        number = int(input('Введите номер контакта для удаления: '))
        res.pop(number)
        #print(res)
        print('Контакт успешно удален')

        with open(file_name, 'w', encoding='utf-8',newline='') as f:
            f_n_writer = DictWriter(f, fieldnames=['Фамилия', 'Имя', 'Номер'])
            f_n_writer.writeheader()
            f_n_writer.writerows(res)


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
        elif command == 'd':
            del_info('phone.csv')
        elif command == 'c':
            change_info('phone.csv')


main()

