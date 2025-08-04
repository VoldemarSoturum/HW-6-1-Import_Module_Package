from requests import * # импортируем все функции из модуля requests
                       # Перед выполнением кода выполняем pip install -r requirements.txt

# Функция для получения информации о пользователе GitHub
# Используем импортированную функцию get из модуля requests
def get_github_user_info(username):
    url = f"https://api.github.com/users/{username}"
    response = get(url)  # используем функцию get из модуля requests, которая теперь в текущем пространстве имен
    # Проверяем, успешен ли запрос
    # Если статус код 200, то возвращаем ответ
    # Если статус код не 200, то возвращаем None
    if response.status_code == 200:
        return response.json()
    else:
        return None
# Пример использования функции
# Здесь мы вызываем функцию get_github_user_info и выводим информацию о пользователе
if __name__ == '__main__':
    user = "VoldemarSoturum"
    info = get_github_user_info(user)
    
    # Вывод информации о пользователе
    # Если информация о пользователе не None, то выводим информацию о пользователе
    # Если информация о пользователе None, то выводим сообщение о том, что пользователь не найден
    if info:
        print(f"[dirty_main] Информация о пользователе {user}:")
        print(f"Имя: {info.get('name')}")
        print(f"Компания: {info.get('company')}")
        print(f"Биография: {info.get('bio')}")
        print(f"Количество публичных репозиториев: {info.get('public_repos')}")
    else:
        print(f"Пользователь {user} не найден")