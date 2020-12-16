"""модуль для роботи з файлами первинних даних
- зчитування та вивід на екран
"""

"""модуль зчитує первинні файли для обробки
"""

def get_dovidniks():
    """повертає дані про ринкові ціни  з файла `dovidnik.txt`

    Returns:
        dovidniks_list: список ринків
    """

    with open("./data/dovidniks.txt") as dovidniks_file:
        from_file = dovidniks_file.readlines()

    dovidniks_list = []
    for line in from_file:
        line_list = line.split(';')
        dovidniks_list.append(line_list)

    return dovidniks_list


def get_danies():
    """повертає список ринків з файлу danie.txt

    Returns:
        danies_file: список данних ринків
    """
    
    with open('.\\ICS-5_Pytulko\\data\\danies.txt') as danies_file:
        from_file = danies_file.readlines()

    
    # розбити строку на реквізити та перетворити формати (при потребі)
    
    # список-накопичувач
    danies_list = []    
    
    for line in from_file:
        line_list = line.split(';')
        line_list[3] = int(line_list[3])
        line_list[4] = float(line_list[4])
        danies_list.append(line_list)

    return danies_list


def show_dovidniks(dovidniks):
    """виводить список ринкових цін по заданому інтервалу кодів

    Args:
        dovidniks (list): список довідника
    """

    # задати інтервал виводу
    dovidnik_code_from = input("З якого кода клієнта? ")
    dovidnik_code_to   = input("По який кода клієнта? ")

    lines_found = 0

    for dovidnik in dovidniks:
        if dovidnik_code_from <= dovidnik[0] <= dovidnik_code_to:
            print ("код: {:5} назва: {:15}".format(dovidnik[0],dovidnik[1]))
            lines_found += 1

    if lines_found == 0:
        print("Клієнтів по Вашому запиту не знайдено") 


def show_danies(danies):
    """виводить список ринків на екран

    Args:
        danies (list): список ринків
    """

    for danie in danies:
        print("Дата: {:13} Код ринку {:5} Ціна картоплі: {:4} Ціна капусти: {:4} Ціна цибулі: {:4}"
            .format(danie[0], danie[1], danie[2], danie[3], danie[4]))

# dovidniks = get_dovidniks()   
#show_dovidniks(dovidniks)

#danies = get_danies()
#show_danies(danies)

