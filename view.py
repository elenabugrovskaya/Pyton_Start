def main_menu():
    commands = ['Показать все контакты',
                'Открыть файл',
                'Сохранить файл',
                'Новый контакт',
                'Изменить контакт',
                'Удалить контакт',
                'Найти контакт',
                'Выйти из программы']
    for i in range(len(commands)):
        print(f'{i+1}. {commands[i]}')
    user_input = int(input('\nВведите пункт меню: '))
    return user_input

def show_contacts(phone_book:list):
    if len(phone_book)>0:
        for i in phone_book:
            print(f"{i[0]} {i[1]} ({i[2]})")
    else:
        print("Телефонная книга пуста или не загружена")

def load_success():
    print('Телефонная книга загружена успешно')

def save_success():
    print('Телефонная книга сохранена успешно')

def new_contact():
    name = input("Введите Имя и Фамилию контакта: ")
    number = input("Введите номер контакта: ")
    comment = input("Введите коментарий: ")
    return name, number, comment

def find_contact():
    search = input('Введите искомое значение: ')
    return search

def change_contact():
    change_name = input("Введите контакт для редактирования: ")
    return change_name

def del_contact():
    del_name = input("Введите контакт для удаления: ")
    return del_name

def del_line_phone_book(name):
    print(f'Контакт {name} удален из телефонной книги')
