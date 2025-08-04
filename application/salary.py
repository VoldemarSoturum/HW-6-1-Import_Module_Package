from datetime import datetime #Импортируем модуль дата/тайм
                              #Для получения текущих даты и времени.
#Функция для расчёта и вывода информации о ЗП сотрудников
def calculate_salary():
    current_date = datetime.now().strftime("%d.%m.%Y")
    print(f"[{current_date}] Расчет зарплат выполнен")
    print("Начислено: 1 250 000 руб.")
    print("Удержано: 162 300 руб.")
    print("К выплате: 1 087 700 руб.")