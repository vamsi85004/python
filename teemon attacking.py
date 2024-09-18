class Teemo:
    def __init__(self, name, attack_damage):
        self.name = name
        self.attack_damage = attack_damage

    def attack(self, enemy):
        enemy.take_damage(self.attack_damage)
        print(f"{self.name} attacks {enemy.name} for {self.attack_damage} damage!")

class Enemy:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def take_damage(self, damage):
        self.health -= damage
        if self.health <= 0:
            print(f"{self.name} has been defeated!")
        else:
            print(f"{self.name} has {self.health} health remaining.")

# Example usage
teemo = Teemo("Teemo", 35)
enemy = Enemy("Enemy Champion", 100)

# Simulate multiple attacks
for turn in range(1, 4):
    print(f"\nTurn {turn}:")
    teemo.attack(enemy)
