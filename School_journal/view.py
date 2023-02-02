def main_menu():
    command = ["Показать журнал",
               "Показать оценки по предмету",
               "Показать оценки по ученику",
               "Показать оценки по предмету и по ученику",
               "Добавить оценку",
               "Выйти из программы"]
    print("Список возможных действий с классным журналом: ")
    for i in range(len(command)):
        print(f"\t{i + 1}.{command[i]}")
    user_input = int(input("\nВведите номер действия: "))
    return user_input


def open_class():
    num_class = input('\nВведите номер класса : ')
    print("")
    return num_class


def show_journal(dict_class: dict, cls: str):
    print("")
    print(f'  Журнал "{cls}" класса')
    for k, v in dict_class.items():
        print(f"{k}")
        for k1, v1 in v.items():
            print(f"\t{k1}\t{','.join(v1)}")
    print("")
    stop = input("Нажмите enter для возврата в меню")
    print("")


def open_subject(dict_class: dict, cls: str):
    subject_list = list(k for k in dict_class.keys())
    print(f'Список предметов "{cls}" класса: ')
    for i in range(len(subject_list)):
        print(f"\t{i + 1}.{subject_list[i]}")
    user_input_sbj = int(input("\nВведите номер предмета: "))
    print("")
    return user_input_sbj


def show_subject(dict_class: dict, cls: str, uis: int):
    print("")
    subject_list = list(k for k in dict_class.keys())
    subject_name = subject_list[uis - 1]
    print(f'Журнал "{cls}" класса')
    print(f'  Предмет: {subject_name}')
    for k, v in dict_class[subject_name].items():
        print(f"\t{k}\t{','.join(v)}")
    print("")
    stop = input("Нажмите enter для возврата в меню")
    print("")


def open_student(dict_class: dict, cls: str):
    student_list = []
    for k, v in dict_class.items():
        for key in v.keys():
            if key not in student_list:
                student_list.append(key)
    print(f'Список учеников "{cls}" класса: ')
    for i in range(len(student_list)):
        print(f"\t{i + 1}.{student_list[i]}")
    user_input_std = int(input("\nВведите номер ученика: "))
    print("")
    return user_input_std


def show_student(dict_class: dict, cls: str, uis: int):
    print("")
    student_list = []
    for k, v in dict_class.items():
        for key in v.keys():
            if key not in student_list:
                student_list.append(key)
    student_name = student_list[uis - 1]
    print(f'Журнал "{cls}" класса')
    print(f'  Ученик: {student_name}')
    for k, v in dict_class.items():
        print(f"\t{k}\t{','.join(v[student_name])}")
    print("")
    stop = input("Нажмите enter для возврата в меню")
    print("")


def show_subject_student(dict_class: dict, cls: str, uis1: int, uis2: int):
    student_list = []
    for k, v in dict_class.items():
        for key in v.keys():
            if key not in student_list:
                student_list.append(key)
    subject_list = list(k for k in dict_class.keys())
    student_name = student_list[uis2 - 1]
    subject_name = subject_list[uis1 - 1]
    print(f'Журнал "{cls}" класса')
    print(
        f'Оценки ученика {student_name} по предмету {subject_name}:\t{",".join(dict_class[subject_name][student_name])}')
    print("")


def Get_bal():
    change_bal = input("Какую оценку поставить: ")
    print("")
    return change_bal

