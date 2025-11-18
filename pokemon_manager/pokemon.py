class Pokemon:
    '''Создание класса Покемон с данными о конкретных видах.'''

    def init(self, name, abilities, types, stats, height, weight, moves):
        self.name = name
        self.abilities = abilities
        self.types = types
        self.stats = stats
        self.height = height
        self.weight = weight
        self.moves = moves
        self.health = stats['hp']  # Текущее здоровье для боя
    
    def take_damage(self, damage):
        """Нанести урон покемону."""
        self.health = max(0, self.health - damage)
        return self.health
    
    def is_fainted(self):
        """Проверить, не лишился ли покемон сознания."""
        return self.health <= 0
    
    def restore_health(self):
        """Восстановить здоровье покемона."""
        self.health = self.stats['hp']
    
    def get_attack_power(self):
        """Узнать силу атаки покемона."""
        return self.stats['attack']
    
    def get_defense(self):
        """Узнать защиту покемона."""
        return self.stats['defense']
    
    def str(self):
        return f"{self.name} (Тип: {', '.join(self.types)})"
    
    def get_detailed_info(self):
        """Получить подробную информацию о покемоне"""
        info = f"""
=== {self.name} ===
Типы: {', '.join(self.types)}
Способности: {', '.join(self.abilities)}
Рост: {self.height / 10} м
Вес: {self.weight / 10} кг

Характеристики:
  - HP: {self.stats['hp']}
  - Атака: {self.stats['attack']}
  - Защита: {self.stats['defense']}
  - Спец. Атака: {self.stats['special-attack']}
  - Спец. Защита: {self.stats['special-defense']}
  - Скорость: {self.stats['speed']}

Доступные атаки: {', '.join(self.moves[:5])}...
"""
        return info