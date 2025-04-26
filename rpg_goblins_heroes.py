#rpg_goblins_heroes
class Character:
    def __init__(self, name, health=10, power=5):
        self.name = name
        self.health = health
        self.power= power
        self.weapons = []
    
    def attack(self, enemy):
        print(f"{self.name} attack {enemy.name}")
        enemy.health -= self.power
    
    #def health(self, enemy):
        #self.health += enemy.power
    
    def is_alive(self):
        return self.health > 0
        
class Hero(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health=health, power=power)

class Goblin(Character):
    def __init__(self, name, health, power):
        super().__init__(name, health=health, power=power)

hero = Hero("Ellen Ripley", 10, 5)
goblin = Goblin("Norman Osborn", 10, 5) 

def main():
    while hero.is_alive() and goblin.is_alive():
        print("you have %d health and %d power" % (hero.health, hero.power))
        print(f"{goblin.name} has {goblin.health} and {goblin.power} power")
        print("Do you have what it takes to be the hero? ")
        print("""
            %s's stats:
            Health: %d
            Attack Power: %d
            """ % (hero.name, hero.health, hero.power))
        
        choice = (input("""
            1. Fight
            2. Flee...coward
            3. Do Nothing
            """))
        if choice == "1":
            hero.attack(goblin)
            print("the damage %d to %s" % (hero.power, goblin.name))
            if not goblin.is_alive():
                print(f"The {goblin.name} is deceased")
        elif choice == "2":
            break
        elif choice == "3":
            pass
        else:
            print("invalid choice, choose better")
            continue

        print("""
            %s's stats:
            Health: %d
            Power: %d
            """ % (goblin.name, goblin.health, goblin.power))

        choice = (input("""
            1. Fight with 
            2. Flee
            3. Do Nothing
            """))
        if choice == "1":
            goblin.attack(hero)
            print("the damage to %s to %d" % (hero.name, hero.power))
            if not hero.is_alive():
                print(f"{hero.name} has been finished")
        elif choice == "2":
            break
        elif choice == "3":
            pass
        else:
            print("invalid choice, heroes turn")
            pass

main()