import pyjokes # Импортируем библиотеку pyjokes для получения шуток
               # Перед выполнением кода выполняем pi  




def get_jokes(language='en', category='neutral', count=3):
    """Получить список программистских шуток"""
    jokes = []
    # Получаем шутки с помощью pyjokes
    # Параметры: язык, категория и количество шуток
    for _ in range(count):
        joke = pyjokes.get_joke(language=language, category=category)
        jokes.append(joke)
    return jokes
# Пример использования функции
# Здесь мы вызываем функцию get_jokes и выводим шутки
if __name__ == '__main__':
    print("=== Программистские шутки ===")
    
    # Получаем шутки
    jokes = get_jokes(language='ru', count=13)
    
    # Выводим шутки с нумерацией
    for i, joke in enumerate(jokes, 1):
        print(f"\nШутка #{i}:")
        print(joke)
    
    print("\nХорошего дня и отличного настроения! 😄")