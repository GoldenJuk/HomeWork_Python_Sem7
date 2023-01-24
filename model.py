phone_book = []
path = 'phone_book.txt'

def get_phone_book():
    global phone_book
    return phone_book

def update_phone_book(contact: list):
    global phone_book
    phone_book.append(contact)

def open_phone_book():
    global phone_book
    global path 
    if phone_book ==[]:
        with open(path,'r', encoding='utf-8') as file:
            data = file.readlines()
            for line in data:
                phone_book.append(line.strip().split(';'))
          
def save_phone_book():
    global phone_book
    global path

    if len(phone_book) > 0:
        contact = ''
        for line in phone_book:
            contact += f'{";".join(line)}\n'
        with open(path, 'w', encoding='utf-8') as file:
            file.write(contact)

def search_contact(contact:str):
    global phone_book
    search_result = []
    for line in phone_book:
        for item in line:
            if contact in item:
                search_result.append(line)
                break
    return search_result         

def delete_contact(contact):
    global phone_book
    for i in range (len(phone_book)):
        if contact[0] == phone_book[i]:
            phone_book.remove(phone_book[i])
            break
 
def change_contact(old_contact, new_contact):
    for i in range (len(phone_book)):
            if old_contact[0] == phone_book[i]:    
                phone_book[i] = new_contact
                break

def output_check():
    global phone_book
    old_phone_book = []
    with open(path,'r', encoding='utf-8') as file:
        data = file.readlines()
        for line in data:
            old_phone_book.append(line.strip().split(';'))
    if old_phone_book == phone_book:
        flag = True
    else:
        flag = False
    return flag    
        