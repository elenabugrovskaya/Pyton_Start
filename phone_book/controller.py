import view
import model

def start():
    user_choice = 0
    while user_choice != 8:
        user_choice = view.main_menu()
        match user_choice:
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book)
            case 2:
                model.open_phone_book()
                view.load_success()
            case 3:
                model.save_phone_book()
                view.save_success()
            case 4:
                new = list(view.new_contact())
                model.update_phone_book(new)
            case 5:
                old_name = view.change_contact()
                new_name = view.new_contact()
                model.renaming_contact(old_name, new_name)
            case 6:
                del_cont = view.del_contact()
                model.delete_contact(del_cont)
                view.del_line_phone_book(del_cont)
            case 7:
                search = view.find_contact()
                result = model.search_contact(search)
                view.show_contacts(result)


