from work_w_file import write, read_all, get_by_name, alter_data, remove_data

def choose(choice):
    if choice == '1': write(input("Введите ваши данные, например:(Фамилия Имя Отчество Телефон) "))
    if choice == "2": read_all()
    if choice == "3": get_by_name(input("Введите имя, фамилию, отчество "))
    if choice == "4": alter_data(input('Введите данные, которые хотите заменить '))
    if choice == "5": remove_data(input('Введите данные, которые хотите удалить '))
    if choice == "6": exit()

def print_instructions():
    return print('Выберите действие: \n 1 - Запись данных в файл \n 2 - Печать всех данных \n '
                 '3 - Поиск по фамилии \n 4 - Замена данных \n '
                 '5 - Удаление данных \n 6 - Выход \n')