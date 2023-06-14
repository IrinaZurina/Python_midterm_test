"""Необходимо написать проект, содержащий функционал работы с заметками.
Программа должна уметь создавать заметку, сохранять её, читать список заметок, редактировать заметку,
удалять заметку, делать выборку по дате, выводить на экран выбранную запись.
Заметка должна содержать идентификатор, заголовок, тело заметки и дату/время создания или
последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через точку с запятой)
"""
import pandas as pd
from datetime import datetime

# notebook = pd.DataFrame(columns=['date', 'name', 'body'])
# notebook.to_csv('Notebook.csv', sep=';')


def choose_action(file_name):   # Функция для выбора действия в приложении
    while True:
        print('Что вы хотите сделать?')
        user_choice = input('1 - Создать заметку\n2 - Найти и просмотреть заметку\n3 - Редактировать заметку\n\
4 - Удалить заметку\n5 - Просмотреть список всех заметок\n6 - Просмотреть заметки за конкретные даты\n0 - Выйти из приложения\n')
        print()
        if user_choice == '1':
            add_new_note(file_name)
        elif user_choice == '2':
            find_note(file_name)
        elif user_choice == '3':
            edit_note(file_name)
        elif user_choice == '4':
            delete_note(file_name)
        elif user_choice == '5':
            show_all_notes(file_name)
        elif user_choice == '6':
            show_date_notes(file_name)
        elif user_choice == '0':
            print('До свидания!')
            break
        else:
            print('Неправильно выбрана команда!')
            print()
            continue


def add_new_note(file_name):   # Функция для добавления новой заметки
    name = input('Введите название заметки: ')
    note = input('Введите текст заметки: ')
    date = datetime.now().date()
    new_note = pd.DataFrame({'date': [date], 'name': [name], 'body': [note]}, index=[0])
    notebook = pd.read_csv(file_name, sep=';', index_col=[0])
    notebook = pd.concat([notebook, new_note], ignore_index=True)
    notebook.to_csv(file_name, sep=';')


def search_parameters():   # Функция для поиска нужной заметки. Используется внутри других функций
    print('По какому полю выполнить поиск?')
    search_field = input('1 - по дате\n2 - по названию\n')
    print()
    search_value = None
    if search_field == '1':
        search_value = input('Введите дату для поиска (гггг-мм-дд): ')
        search_field = 'date'
        print()
    elif search_field == '2':
        search_value = input('Введите название заметки для поиска: ')
        search_field = 'name'
        print()
    return search_field, search_value


def find_note(file_name):   # Функция для поиска заметки по заголовку или дате
    search_field, search_value = search_parameters()
    notebook = pd.read_csv(file_name, sep=';', index_col=[0])
    found_notes = notebook.loc[notebook[search_field].str.contains(search_value)]
    if len(found_notes) == 0:
        print('Такой заметки не найдено!')
    else:
        print(found_notes)
    print()


def edit(notebook, index_to_edit):   # Функция для редактирования конкретного поля, является частью функции edit_note
    field_to_edit = input('Что вы хотите изменить? 1 - Название, 2 - Содержание:')
    if field_to_edit == '1':
        notebook.loc[index_to_edit, 'name'] = input('Введите новое название:')
    else:
        notebook.loc[index_to_edit, 'body'] = input('Введите новое содержание:')
    notebook.loc[index_to_edit, 'date'] = datetime.now().date()


def edit_note(file_name):   # Функция для внесения изменений в заметку. Дата обновляется автоматически
    print('Какую заметку вы хотите изменить? Выполните поиск.')
    search_field, search_value = search_parameters()
    notebook = pd.read_csv(file_name, sep=';', index_col=[0])
    found_notes = notebook.loc[notebook[search_field].str.contains(search_value)]
    if len(found_notes) == 0:
        print('Такой заметки не найдено!')
    elif len(found_notes) == 1:
        print(found_notes)
        print()
        answer = input('Вы хотите изменить эту заметку? (да/нет)')
        if answer == 'да':
            index_to_edit = found_notes.index
            edit(notebook, index_to_edit)
    else:
        print('Найдено несколько заметок:')
        print(found_notes)
        print()
        index_to_edit = int(input('Введите номер заметки из списка: '))
        edit(notebook, index_to_edit)
    notebook.to_csv(file_name, sep=';')
    print()


def delete_note(file_name):   # Функция для удаления заметки
    print('Какую заметку вы хотите удалить? Выполните поиск.')
    search_field, search_value = search_parameters()
    notebook = pd.read_csv(file_name, sep=';', index_col=[0])
    found_notes = notebook.loc[notebook[search_field].str.contains(search_value)]
    if len(found_notes) == 0:
        print('Такой заметки не найдено!')
    elif len(found_notes) == 1:
        print(found_notes)
        print()
        answer = input('Вы хотите удалить эту заметку? (да/нет)')
        if answer == 'да':
            index_to_delete = found_notes.index
            notebook.drop(labels=index_to_delete, axis=0, inplace=True)
    else:
        print('Найдено несколько заметок:')
        print(found_notes)
        print()
        index_to_delete = int(input('Введите номер заметки из списка: '))
        notebook.drop(labels=index_to_delete, axis=0, inplace=True)
    notebook.to_csv(file_name, sep=';')
    print()


def show_all_notes(file_name):   # вывод всех заметок в виде датафрейма
    notebook = pd.read_csv(file_name, sep=';', index_col=[0])
    print(notebook)
    print()


def show_date_notes(file_name):   # Вывод заметок за выбранный интервал дат
    start = datetime.strptime(input('Введите начальную дату (гггг-мм-дд): '), "%Y-%m-%d")
    end = datetime.strptime(input('Введите конечную дату (гггг-мм-дд): '), "%Y-%m-%d")
    notebook = pd.read_csv(file_name, sep=';', index_col=[0])
    notebook['date'] = pd.to_datetime(notebook['date'], format="%Y-%m-%d")
    print(notebook.loc[(notebook['date'] >= start) & (notebook['date'] <= end)])
    print()


# Запуск приложения - страницы выбора действий
if __name__ == '__main__':
    file = 'Notebook.csv'
    choose_action(file)

