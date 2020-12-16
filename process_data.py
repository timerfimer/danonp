"""розрахунок середніх ринкових цін на основні продукти
"""

from data_service import get_danies, get_dovidniks

analiz =  {
    'market_code'        : '',          # код ринку
    'market_name'        : '',          # назва ринку
    'date'               : 00-00-00,    # дата
    'price_of_potato'    : 0.0,         #ціна картошки
    'price_of_cabbage'   : 0.0,         #ціна капусти
    'price_of_onion'     : 0.0,         #ціна цибулі
    'average_price'      : 0.0,         #Середня ціна
}


def create_analiz():
    """
    формування списку аналізу інформації по ринках 
    """
        
    dovidniks = get_dovidniks()
    danies = get_danies()
    
    def get_dovidnik_name(dovidnik_name):
        """повертає назву клієнта по його коду 

        Args:
            dovidnik_code: код ринку
        """

    # Послідовна обробка рядків масиву 'dovidnik'
        for dovidnik in dovidniks: 
            if dovidnik_code == dovidnik[0]:
                return dovidnik[1]

        return "*** назва не знайдена"

    #Список ринкових аналізу ринкових цін, що формується
    analiz_list = []

    # Обробляємо посілодовно кожний рядок 'danie'
    for danie in danies:

        #підготувати робочий словник для рядка 'order'
       analiz_work = analysis.copy()

        # Заповнити робочий словник значеннями  
        analiz_work['market_code'] = danie[0]
        analiz_work['market_name'] = get_dovidnik_name(danie[1])
        analiz_work['date'] = danie[0]
        analiz_work['price_of_potato'] = danie[2]
        analiz_work['price_of_cabbage'] = danie[3]
        analiz_work['price_of_onion'] = danie[4]
        analiz_work['average_price'] = (analiz_work['price_of_potato'] + analiz_work['price_of_cabbage'] + analiz_work['price_of_onion']) // 3))
        # Зробити робочий словник з шаблону

        analiz_list.append(analiz_work)
    return(analiz_list)
create_analiz()
