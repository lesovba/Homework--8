# За основу взял файл, который приложен к семинару. 

def check(text):
    if len(text.split()) == 4:
        if text.split()[3].isdigit():
            return True
        else:
            print("Номер введен неправильно!")
            print("Нужно ввести номер телефона без знака +")
            return False
    else:
        print("Нужно ввести (Фамилию Имя Отчество Номер)!")
        return False

def check_number(tel_number):
    with open("data.txt", "r") as f:
        for line in f:
            if tel_number in line:
                return True
        return False

def write(text):
    if check(text):
        with open("data.txt", "a") as f:
            f.writelines(text)
            f.writelines("\n")
            print("Успешно")
    else:
        return -1


def read_all():
    with open("data.txt", "r") as f:
        for line in f:
            print(line[:-1])


def get_by_name(name):
    with open("data.txt", "r") as f:
        for line in f:
            if name in line:
                print(line)

# Решил, что лучше менять данные произвольно, а не построчно. 
# Так можно будет изменять только те данные, которые некорректны. 
# На вход сразу принимаем данные, которые хотим заменить. 
def alter_data(words):
    f = open ('data.txt', 'r')
    old_data = f.read()
    # Меняем данные на новые с помощью метода replace() и нового input()
    new_data = old_data.replace(words, input("Введите новые данные: "))
    # Записываем измененные данные в файл
    with open ('data.txt', 'w') as f:
        f.write(new_data)

def remove_data(words):
    f = open ('data.txt', 'r')
    old_data = f.read()
    # Заменяем данные пустыми символами
    new_data = old_data.replace(words, "")
    # Записываем измененные данные в файл
    with open ('data.txt', 'w') as f:
        f.write(new_data)
        print("Данные удалены")