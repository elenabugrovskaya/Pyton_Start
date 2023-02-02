import model
import view

def start():
    global journal
    global _class_1
    user_input = 0
    _class_1 = view.open_class()
    journal = model.open_journal(_class_1)
    while user_input != 6:
        user_input = view.main_menu()
        match user_input:
            case 1:
                view.show_journal(journal, _class_1)
            case 2:
                subject_num = view.open_subject(journal, _class_1)
                view.show_subject(journal, _class_1, subject_num)
            case 3:
                student_num = view.open_student(journal, _class_1)
                view.show_student(journal, _class_1, student_num)
            case 4:
                subject_num = view.open_subject(journal, _class_1)
                student_num = view.open_student(journal, _class_1)
                view.show_subject_student(journal, _class_1, subject_num, student_num)
            case 5:
                subject_num = view.open_subject(journal, _class_1)
                student_num = view.open_student(journal, _class_1)
                view.show_subject_student(journal, _class_1, subject_num, student_num)
                bal = view.Get_bal()
                model.append_bal(journal, subject_num, student_num, bal)
                view.show_subject_student(journal, _class_1, subject_num, student_num)
    model.save_journal(_class_1)

