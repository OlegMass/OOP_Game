import time
import random


data = {
    "name": "hero",
    "level": 1,
    "experience": 0,
    "boss_level": 1,
    "life": 100,
    "defense": 20,
    "damage": 30,
    "critical": 10,
    "dodge": 15,
    "ignore_defense": 15    
        }
data_1 = {
    "name": "hero_1",
    "level": 50,
    "experience": 400,
    "boss_level": 14,
    "life": 300,
    "defense": 50,
    "damage": 70,
    "critical": 50,
    "dodge": 50,
    "ignore_defense": 50    
        }
alive=True
creature_num=1


class Creator:
    def __init__(self, name, life, defense, damage):
        self.name = name
        self.level = 1
        self.experience = 0
        self.boss_level = 1
        self.life = life
        self.defense = defense
        self.damage = damage
        self.critical = 10
        self.dodge = 15
        self.ignore_defense = 15

    def attack(self, user):
        name_opp = 'None'
        if random.randint(1,100) <= self.dodge:
            print(f"{user.name} dodge the punch!")
            user.life -= 0
        else:    
            if random.randint(1, 100) <= self.critical:
                print(f"{self.name} made a critical attack!!!")
                if random.randint(1,100) <= self.ignore_defense:
                    print(f"{self.name} ignore defence during attack!")
                    user.life -= self.damage*2 
                user.life -= (self.damage - user.defense)*2
            if random.randint(1,100) <= self.ignore_defense:
                print(f"{self.name} ignore defence during attack!")
                user.life -= self.damage
            user.life -= self.damage - user.defense

    def experiance(self):
        pass


hero = Creator(data_1["name"], data_1["life"], data_1["defense"], data_1["damage"])
hero.level = data_1["level"]
hero.experience = data_1["experience"]
hero.boss_level = data_1["boss_level"]
hero.critical = data_1["critical"]
hero.dodge = data_1["dodge"]
hero.ignore_defense = data_1["ignore_defense"]

creature = Creator('creature', 40, 10, 30)
boss = Creator(
            'Ktulkhu',
            100 + 10*hero.boss_level,
            20 + 2*hero.boss_level,
            35 + 5*hero.boss_level,
            )

def show(model):
    print(f"""
{model.name}
1 Life: {model.life}
2 Defence: {model.defense}
3 Damage: {model.damage}
4 Critical hit chance: {model.critical}
5 Defence ignoring chance : {model.ignore_defense}  
6 Dodge: {model.dodge}
{f'7 Boss level: {hero.boss_level}' if model.name == 'Ktulkhu' else ''}
""")


def increase_level():
    hero.level+=1
    data["level"] += 1
    print("""
1 Life
2 Defence
3 Damage
4 Critical hit chance
5 Defence ignoring chance   
6 Dodge 
    """)
    option = int(input('What do you want to improve? '))
    if option == 1:
        hero.life+=10
        data["life"] +=10
        print(f"Now you have {hero.life} life")
    elif option == 2:
        hero.defense += 2
        data["defense"] += 2
        print(f"Now you have {hero.defense} defense.")
    elif option == 3:
        hero.damage += 2
        hero["damage"] += 2
        print(f"Now you have {hero.damage} defense.")
    elif option == 4:
        hero.critical += 1
        hero["critical"] += 1
        print(f"Now you have {hero.critical} defense.")
    elif option == 5:
        hero.ignore_defense += 1
        hero["ignore_defense"] += 1
        print(f"Now you have {hero.ignore_defense} defense.")
    elif option == 6:
        hero.dodge += 1
        hero["dodge"] += 1
        print(f"Now you have {hero.dodge} defense.")

    print(f"""
1 Life: {hero.life}
2 Defence: {hero.defense}
3 Damage: {hero.damage}
4 Critical hit chance: {hero.critical}
5 Defence ignoring chance : {hero.ignore_defense}  
6 Dodge: {hero.dodge}
          """)

def increse_boos():
    boss.life = boss.life + 10*hero.boss_level

    boss.defense = boss.defense + 2*hero.boss_level
    boss.damage = boss.damage + 5*hero.boss_level
            
    return boss.life, boss.defense, boss.damage

def attack_boss():
    boss_life = boss.life
    hero_life = hero.life
    version = int(input("""
    1 Show the details of a battle.
    2 Don't show details of a battle
    """))
    if version == 1:
        show(hero)
        show(boss)
        while True:
            input("Press enter to punch an enemy")
            time.sleep(1)
            hero.attack(boss)
            if boss.life <= 0:
                print('You win the boss!')
                boss.life = boss_life  
                hero.boss_level += 1  
                data["boss_level"] += 1
                increse_boos() 
                hero.life = hero_life 
                break
            print(f"Boss has {boss.life} life")
            time.sleep(1)
            print("Boss attacking you too!!!")
            boss.attack(hero)
            if hero.life <= 0:
                print('You are dead!')
                stop_game()
                break
            print(f"You have {hero.life} life.")
    elif version==2:
        while True:
            hero.attack(boss)
            if boss.life <= 0:
                print('You win the boss!')
                boss.life = boss_life   
                hero.boss_level += 1  
                data["boss_level"] += 1
                increse_boos()  
                hero.life = hero_life 
                break
            print(f"Boss has {boss.life} life")
            boss.attack(hero)
            if hero.life <= 0:
                print('You are dead!')
                stop_game()
                break
            print(f"You have {hero.life} life.")
    if hero.boss_level == 100:
        print("""
        
        
        
        Congrats! You win thos game!
        

            Created by Oleg Mass
        
        """)
        stop_game()

def attack_creature():
    global creature_num
    creature_num = int(input("""
        How many Creatures do you want to attack?
    """))
    no_exp = creature_num
    hero_life = hero.life

    version = int(input("""
    1 Show the details of a battle.
    2 Don't show details of a battle
    """))
    life_one_creature = creature.life
    if version == 1:
        show(hero)
        show(creature)
        while True:
            input("Press enter to punch an enemy")
            time.sleep(1)
            hero.attack(creature)
            if creature.life <= 0 and creature_num == 1:
                print('You win!')
                hero.experience += no_exp * 50
                if hero.experience>=hero.level*100:
                    hero.life = hero_life
                    increase_level()
                    hero.experience = 0
                break
            elif creature.life <= 0 and creature_num > 1:
                creature_num -= 1
                print(f"You kill 1 creature and {creature_num} creatures are left ")
                creature.life = life_one_creature
            print(f"Creature has {creature.life} life.")
            time.sleep(1)
            print("Creature attacking you too!!!")
            for i in range(creature_num):
                creature.attack(hero)
                if hero.life <= 0:
                    print('You are dead!')
                    
                    break
                print(f"You have {hero.life} life.")
                
            if hero.life <= 0:
                hero.life = hero_life 
                stop_game()
                break
    elif version==2:
        while True:
            hero.attack(creature)
            if creature.life <= 0 and creature_num == 1:
                print('You win!')
                hero.experience += no_exp * 50
                if hero.experience >= hero.level*100:
                    hero.life = hero_life
                    increase_level()
                    hero.experience = 0
                    
                break
            elif creature.life <= 0 and creature_num > 1:
                creature_num -= 1
                creature.life = life_one_creature
            for i in range(creature_num):
                creature.attack(hero)
                if hero.life <= 0:
                    print('You are dead!')
                break 
            if hero.life <= 0:
                hero.life = hero_life
                stop_game()
                break

def stop_game():
    global alive 
    alive = False
    return alive

def main():
    while alive == True:
        print(""" 
1 Attack creatures
2 Attack Boss
3 Exit
9 Info
""")

        choice = int(input("What do you want to do? "))
        if choice == 1:
            attack_creature()
        elif choice == 2:
            attack_boss()
        elif choice == 9:
            show(hero)
            show(creature)
            show(boss)
        else:
            break

main()







