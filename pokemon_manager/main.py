from team_manager import PokemonTeamManager

def main():
    manager = PokemonTeamManager()
    
    print("=== МЕНЕДЖЕР КОМАНДЫ POKÉMON ===")
    
    while True:
        print("МЕНЮ")
        print("1. Добавить покемона в команду")
        print("2. Удалить покемона из команды")
        print("3. Просмотреть команду")
        print("4. Просмотреть подробную информацию о команде")
        print("5. Найти покемона по имени")
        print("6. Тренировочный бой")
        print("7. Выйти")
        
        choice = input("Выберите действие (1-7): ").strip()
        
        if choice == '1':
            pokemon_name = input("Введите имя покемона для добавления: ").strip()
            manager.add_pokemon(pokemon_name)
        
        elif choice == '2':
            pokemon_name = input("Введите имя покемона для удаления: ").strip()
            manager.remove_pokemon(pokemon_name)
        
        elif choice == '3':
            manager.view_team()
        
        elif choice == '4':
            manager.view_detailed_info()
        
        elif choice == '5':
            pokemon_name = input("Введите имя покемона для поиска: ").strip()
            manager.find_pokemon(pokemon_name)
        
        elif choice == '6':
            if manager.get_team_size() < 2:
                print("Для боя нужно как минимум 2 покемона в команде.")
            else:
                manager.view_team()
                pokemon1 = input("Введите имя первого покемона: ").strip()
                pokemon2 = input("Введите имя второго покемона: ").strip()
                manager.train_battle(pokemon1, pokemon2)
        
        elif choice == '7':
            print("До свидания!")
            break
        
        else:
            print("Такого варианта не существует. Пожалуйста, выберите от 1 до 7.")

if __name__ == "main":
    main()