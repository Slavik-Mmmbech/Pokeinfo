"""
МОДУЛЬ: PokeAPI Client - Работа с API покемонов

ВЕРСИЯ: 1.0
АВТОР: [Ваше имя]
ДАТА СОЗДАНИЯ: [Текущая дата]

ОПИСАНИЕ:
Этот модуль предоставляет функции для взаимодействия с PokeAPI - бесплатной RESTful API,
содержащей подробную информацию о покемонах. Модуль позволяет получать базовые списки
покемонов и детальную информацию о конкретных покемонах.

ИСПОЛЬЗУЕМЫЕ БИБЛИОТЕКИ:
- requests: Для выполнения HTTP-запросов к PokeAPI.
"""

import requests


def get_pokemon_list():
    """
    Получить список первых 20 покемонов из PokeAPI.
    
    ФУНКЦИОНАЛ:
        Выполняет GET-запрос к эндпоинту /pokemon PokeAPI с ограничением в 20 записей,
        обрабатывает ответ и выводит форматированный список покемонов с нумерацией.
    
    АРГУМЕНТЫ:
        Нет
    
    ВОЗВРАЩАЕМОЕ ЗНАЧЕНИЕ:
        None (функция выводит результат непосредственно в консоль)
    
    ПРОЦЕСС РАБОТЫ:
        1. Формирование URL для запроса
        2. Выполнение HTTP GET-запроса
        3. Парсинг JSON-ответа
        4. Извлечение списка покемонов из поля 'results'
        5. Форматированный вывод с нумерацией
    
    ПРИМЕР ИСПОЛЬЗОВАНИЯ:
        >>> get_pokemon_list()
        Список первых 20 покемонов:
        1. bulbasaur
        2. ivysaur
        ...
    """
    url = "https://pokeapi.co/api/v2/pokemon?limit=20"
    
    response = requests.get(url)

    data = response.json()
    pokemons = data['results']
        
    print("Список первых 20 покемонов:")
    for i, pokemon in enumerate(pokemons, 1):
        print(f"{i}. {pokemon['name']}")


def get_pokemon_details(pokemon_name):
    """
    Получить детальную информацию о конкретном покемоне из PokeAPI.
    
    ФУНКЦИОНАЛ:
        Выполняет GET-запрос к эндпоинту /pokemon/{name} PokeAPI, извлекает ключевую
        информацию о покемоне и выводит ее в удобочитаемом формате.
    
    АРГУМЕНТЫ:
        pokemon_name (str): Имя покемона на английском языке (регистронезависимо)
    
    ВОЗВРАЩАЕМОЕ ЗНАЧЕНИЕ:
        None (функция выводит результат непосредственно в консоль)
    
    ИЗВЛЕКАЕМАЯ ИНФОРМАЦИЯ:
        - Имя покемона (name)
        - Типы (types) - может быть несколько
        - Вес (weight) в условных единицах
        - Рост (height) в условных единицах  
        - Способности (abilities)
    
    ПРОЦЕСС РАБОТЫ:
        1. Формирование URL с именем покемона (в нижнем регистре)
        2. Выполнение HTTP GET-запроса
        3. Обработка возможных HTTP ошибок (404 и др.)
        4. Парсинг JSON-ответа и извлечение нужных полей
        5. Форматированный вывод информации
    """
    url = f"https://pokeapi.co/api/v2/pokemon/{pokemon_name.lower()}"
    
    try:
        response = requests.get(url)
        
        data = response.json()

        name = data['name']
        types = [type_data['type']['name'] for type_data in data['types']]
        weight = data['weight']
        height = data['height']
        abilities = [ability_data['ability']['name'] for ability_data in data['abilities']]
        
        print(f"Информация о покемоне {name}:")
        print(f"Имя: {name}")
        print(f"Тип: {', '.join(types)}")
        print(f"Вес: {weight}")
        print(f"Рост: {height}")
        print(f"Способности: {', '.join(abilities)}")
        
    except requests.exceptions.HTTPError:
        print(f"Покемон '{pokemon_name}' не найден!")
