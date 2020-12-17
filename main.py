""" головний модуль додатку 
- вивід на екран та в файл розрахункових даних 
- виводити на екран файли первинних даних
"""

import os
from process_data import create_analiz
from data_service import show_danies, show_dovidniks, get_danies, get_dovidniks

MAIN_MENU = \
"""
~~~~~~~~~ ОБРОБКА АНАЛІЗІВ СЕРЕДНІХ РИНКОВИХ ЦІН НА ОСНОВНІ ПРОДУКТИ СПОЖИВЧОГО КОШИКА ~~~~~~~~~~


1 - вивід аналізів ринків
2 - запис аналізів ринків у файл
3 - вивід стат. данних 
4 - вивід довідника
0 - завершити роботу
-------------------
"""

TITLE = "АНАЛІЗ СЕРЕДНІХ РИНКОВИХ ЦІН НА ОСНОВІ ПРОДУКТІВ СПОЖИВЧОГО КОШИКА"
HEADER = \
'''
=======================================================================================================================================
| Код ринку     |   Найменування ринку       |     Дата     | Ціна (картопля) |   Ціна (капуста)  |  Ціна (цибуля)  | Середня ціна |
=======================================================================================================================================
'''
FOOTER = \
'''
=======================================================================================================================================
'''

STOP_MESSAGE = "Нажміть будь-яку клавішу для продовження"

def show_analiz(analiz_list):
    """виводить сформовані аналізи на екран у вигляді таблиці
    Args:
        analiz_list ([type]): список аналізів середніх ринкових цін
    """
    
    print(f'\n\n{TITLE:^90}')
    print(HEADER)
    
    for analiz in analiz_list:
        print(f"{analiz['market_code']:>16.5}",
              f"{analiz['market_name']:18}",
              f"{analiz['date']:>24}",
              f"{analiz['price_of_potato']:>18.2f}"
              f"{analiz['price_of_cabbage']:>19.2f}"
              f"{analiz['price_of_onion']:>19.2f}"
              f"{analiz['average_price']:>17.2f}"
              )


    print(FOOTER)


def write_analiz(analiz_list):
    """пише список аналізів середніх ринковх цін у файл
    Args:
        analiz_list ([type]): список аналізів
    """
    
    with open('analiz.txt', "w") as analiz_file:
        for analiz in analiz_list:
            line = \
                str(analiz['market_code']) + ';' +      \
                analiz['market_name'] + ';' +      \
                analiz['date']  + ';' +      \
                str(analiz['price_of_potato'])  + ';' +   \
                str(analiz['price_of_cabbage'])  + ';' + \
                str(analiz['price_of_onion'])  + ';' + \
                str(analiz['average_price']) + '\n' 
                
            analiz_file.write(line)
        
        
        print("Файл заявок сформовано ...")
    

while True:
    
    # вивід головного меню
    os.system('cls')
    print (MAIN_MENU)
    command_number = input('Введіть номер команди: ')

    # обробка команд користувача
    if command_number == '0':
        print("\nПрограма завершила роботу")
        exit(0)
    
    elif command_number == '1':
        analiz_list = create_analiz()
        show_analiz(create_analiz())
        input(STOP_MESSAGE)
    
    elif command_number == '2':
        analiz_list = create_analiz()
        write_analiz(analiz_list)
        input(STOP_MESSAGE)
    
    elif command_number == '3':
        show_danies(get_danies())
        input(STOP_MESSAGE)
    
    elif command_number == '4':
        show_dovidniks(get_dovidniks())
        input(STOP_MESSAGE)
        
    else:
        print("невірний номер команди...")
        input(STOP_MESSAGE)