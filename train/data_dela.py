from datetime import datetime

def work_data( data_plan = datetime(2024,5,28)):
    
    data_now = datetime.now()
    data_now = datetime(
        data_now.year,
        data_now.month,
        data_now.day,


    )
    


    data_vchera = datetime(2024,5,27)
    data_tomorow = datetime(2024,5,29)
    
    # esli data_plan ravna data_vchera vernut "Вчера"
    # esli data_plan ravna data_tomorow vernut "Завтра"
    # esli data_plan ravna data_now vernut "Сегодня"

    
    if data_plan == data_vchera:
        return('Вчера')
    elif data_plan == data_tomorow:
        return('Завтра')
    elif data_plan == data_now:
        return('Сегодня')    
        


    return('Не знаю когда')



''' while cifra == int:
        if data_now < data_tomorow and data_now > data_vchera:
            print()
        else:
            print('Vvedite cifry')'''
        