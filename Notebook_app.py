"""Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список
заметок, редактировать заметку, удалять заметку, делать выборку по дате, выводить на
экран выбранную запись.
Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через точку с запятой)
"""
import pandas as pd
from datetime import datetime


# notebook = pd.DataFrame({'date': [], 'name': [], 'body': []})
# notebook.to_csv('Notebook')


def choose_action(file_name):
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Создать заметку\n2 - Найти и просмотреть заметку\n3 - Редактировать заметку\n\
4 - Удалить заметку\n5 - Просмотреть список всех заметок\n6 - Просмотреть заметки за конкретные даты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            add_new_note(file_name)
        # elif user_choice == '2':
        #     contact_list = read_file_to_dict(phonebook)
        #     find_number(contact_list)
        # elif user_choice == '3':
        #     add_phone_number(phonebook)
        # elif user_choice == '4':
        #     change_phone_number(phonebook)
        # elif user_choice == '5':
        #     delete_contact(phonebook)
        # elif user_choice == '6':
        #     show_phonebook(phonebook)
        # elif user_choice == '0':
        #     print('До свидания!')
        #     break
        # else:
        #     print('Неправильно выбрана команда!')
        #     print()
        #     continue


def add_new_note(file_name):
    name = input('Введите название заметки: ')
    note = input('Введите текст заметки: ')
    date = datetime.now().date()
    notebook = pd.read_csv(file_name)
    notebook.append({'date': date, 'name': name, 'body': note})
    notebook.to_csv('Notebook')


if __name__ == '__main__':
    file = 'Notebook.csv'
    choose_action(file)

