import view, model

def start():
    user_choice = 0
    while True:
        user_choice = view.main_menu()
        match user_choice:
            
            case 1:
                phone_book = model.get_phone_book()
                view.show_contacts(phone_book,user_choice)
            
            case 2:
                model.open_phone_book()
                view.show_result_choice(user_choice)
            
            case 3:
                view.show_contacts(phone_book,user_choice)
                confirmation = view.get_confirmation()
                if confirmation:
                    model.save_phone_book()
                    view.show_result_choice(user_choice)
                                  
            case 4:
                contact = view.new_contact()
                model.update_phone_book(list(contact))
                view.show_result_choice(user_choice)
            
            case 5:
                contact_old = view.change_contact()
                result = model.search_contact(contact_old)
                view.show_contacts(result, user_choice)
                if result != []:
                    flag = view.get_clarification(result)
                    if flag:
                        confirm = view.get_confirmation()
                        if confirm:
                            contact_new = list(view.new_contact())
                            model.change_contact(result, contact_new)

            case 6:
                contact = view.del_contact()
                result = model.search_contact(contact)
                view.show_contacts(result, user_choice)
                if result != []:
                    flag = view.get_clarification(result)
                    if flag:
                        confirm = view.get_confirmation()
                        if confirm:
                            model.delete_contact(result)

            case 7:
                contact = view.find_contact()
                result = model.search_contact(contact)
                view.show_contacts(result,user_choice)

            case 8:
                identity = model.output_check()
                if identity:
                    break
                else:
                    phone_book = model.get_phone_book()
                    if len(phone_book) > 1:
                        view.show_contacts(phone_book,user_choice)
                        view.identity_test(identity)
                        confirm = view.get_confirmation()
                        if confirm:
                            model.save_phone_book()
                            break
                    else:
                        break                            



