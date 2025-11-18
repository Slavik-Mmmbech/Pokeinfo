import requests
from pokemon import Pokemon

class PokemonTeamManager:
    '''Класс создается для управления командой покемонов.'''
    BASE_URL = "https://pokeapi.co/api/v2/pokemon/"
    
    def init(self):
        self.team = []
        self.max_team_size = 6
    
    def fetch_pokemon_data(self, pokemon_name):
        """Получить данные покемона из API"""
        try:
            response = requests.get(f"{self.BASE_URL}{pokemon_name.lower()}")
            if response.status_code == 200:
                return response.json()
            else:
                print(f"Покемон '{pokemon_name}' не найден.")
                return None
        except requests.exceptions.RequestException as e:
            print(f"Ошибка при подключении к API: {e}")
            return None
    
    def create_pokemon_from_data(self, data):
        """Создать объект Pokemon из данных API"""
        name = data['name'].capitalize()
        abilities = [ability['ability']['name'] for ability in data['abilities']]
        types = [type_data['type']['name'] for type_data in data['types']]
        
        stats = {}
        for stat in data['stats']:
            stat_name = stat['stat']['name']
            stats[stat_name] = stat['base_stat']
        
        height = data['height']
        weight = data['weight']
        moves = [move['move']['name'] for move in data['moves'][:10]]  # Берем первые 10 атак
        
        return Pokemon(name, abilities, types, stats, height, weight, moves)
    
    def add_pokemon(self, pokemon_name):
        """Добавить покемона в команду"""
        if len(self.team) >= self.max_team_size:
            print(f"Команда уже полна! Максимум {self.max_team_size} покемонов.")
            return False
        
        # Проверяем, есть ли уже такой покемон в команде
        if any(pokemon.name.lower() == pokemon_name.lower() for pokemon in self.team):
            print(f"Покемон '{pokemon_name}' уже есть в команде!")
            return False
        
        data = self.fetch_pokemon_data(pokemon_name)
        if data:
            pokemon = self.create_pokemon_from_data(data)
            self.team.append(pokemon)
            print(f"Покемон {pokemon.name} добавлен в команду!")
            return True
        return False
    
    def remove_pokemon(self, pokemon_name):
        """Удалить покемона из команды"""
        for i, pokemon in enumerate(self.team):
            if pokemon.name.lower() == pokemon_name.lower():
                removed_pokemon = self.team.pop(i)
                print(f"Покемон {removed_pokemon.name} удален из команды!")
                return True
        
        print(f"Покемон '{pokemon_name}' не найден в команде!")
        return False
    
    def view_team(self):
        """Просмотреть всю команду"""
        if not self.team:
            print("Команда пуста!")
            return
        
        print(f"\n=== ВАША КОМАНДА ({len(self.team)}/{self.max_team_size}) ===")
        for i, pokemon in enumerate(self.team, 1):
            print(f"{i}. {pokemon}")
    
    def view_detailed_info(self):
        """Просмотреть подробную информацию о всех покемонах в команде"""
        if not self.team:
            print("Команда пуста!")
            return
        
        for pokemon in self.team:
            print(pokemon.get_detailed_info())
    
    def find_pokemon(self, pokemon_name):
        """Найти покемона по имени"""
        for pokemon in self.team:
            if pokemon.name.lower() == pokemon_name.lower():
                print(f"Покемон найден!")
                print(pokemon.get_detailed_info())
                return pokemon
        
        print(f"Покемон '{pokemon_name}' не найден в команде!")
        return None
    
    def train_battle(self, pokemon1_name, pokemon2_name):
        """Устроить тренировочный бой между двумя покемонами"""