'''
This is a RPG style game with no GUI
developed by Sieg and completed by Ademola during 
a bootcamp organized by GDSC LAUTECH in
collaboration with BuggyBillions
'''


import hashlib
from random import randint, choice
print('Welcome to Avengers')

# authentication
username = input('Enter a username: ')
password = input('Enter a password: ')
confirm_pass = input('Confirm the password above: ')

# password validation
while password != confirm_pass:
    print('Passwords do not match, enter passwords again')
    # Enter passwords
    password = input('Enter a password: ')
    confirm_pass = input('Confirm the password above: ')
    if password == confirm_pass:
        break
encoded_pass = hashlib.md5(password.encode())

# Profile creation
class Player:
    def __init__(self, item, attack, defense, health, agility):
        self.item = item
        self.attack = attack
        self.defense = defense
        self.health = health
        self.agility = agility
    
    def print_player(self):
        player = print(f'''
        Profile has been successfully created
        Item chosen by system is {self.item}
        name = {username}
        attack = {self.attack}
        defense = {self.defense}
        health = {self.health}
        agility = {self.agility}
        ''')
        return player
items = ['axe', 'sword', 'knife', 'bat']
chosen_item = choice(items)
created_player = Player(chosen_item, randint(10, 20), randint(15, 25), randint(700, 1200), randint(30, 60))
created_player.print_player()

# define animal stats
class Animal:
    def __init__(self, type, attack, defense, health, agility):
        self.type = type
        self.attack = attack
        self.defense = defense
        self.health = health
        self.agility = agility
        
    def print_animal(self):
        animal = print(f'You met a {self.type} with attack {self.attack}, defense {self.defense}, health {self.health}, agility {self.agility}')
        return animal

class Monster:
    def __init__(self, type, attack, defense, health, agility, magic):
        self. type = type
        self.attack = attack
        self.defense = defense
        self.health = health
        self.agility = agility
        self.magic = magic

    def print_monster(self):
        monster = print(f'You met a {self.type} with attack {self.attack}, defense {self.defense}, health {self.health}, agility {self.agility}, magic {self.magic}')
    
    def print_monster_goblin(self):
        goblin = print(f'You met 6 {self.type} each with attack {self.attack}, defense {self.defense}, health {self.health}, agility {self.agility}, magic {self.magic}')
        
        return Monster

print('You are presented two paths, pick one: LEFT or RIGHT')
path = input('Choose a path: ').upper()
if path == 'LEFT':
    wolf = Animal('wolf', randint(30, 50), randint(10, 20), randint(200, 300), randint(10, 30))
    wolf.print_animal()
    while wolf.health > 0:
        wolf.health -= choice(range(1, created_player.attack))
        print(f' Wolf {wolf.health}')
        created_player.health -= choice(range(1, wolf.attack))
        print(f'Player {created_player.health}')
        if created_player.health <= 0:
            print('Sorry you died, End of game')
            break
    print('You defeated the wolf and some items got dropped')
    print('Wolf dropped paladin\'s helmet and goblin boots')
    paladins_helmet = 10
    goblin_boots = 15
    created_player.defense += paladins_helmet
    created_player.agility += goblin_boots
    created_player.health += goblin_boots
    print(created_player.print_player())

elif path == 'RIGHT':
    print(f''' On your journey through this path {username}, you have been blessed
    by the Gods ! and the following items have been gifted unto you
    Mjlinor and Saber
    ''')

    Mjlinor = 100
    if created_player.health >= 500:
        Saber = 350
    else:
        Saber = 190
    created_player.agility += Mjlinor
    created_player.attack += Saber
    print(created_player.print_player())

    print(f'''
    the path you tread is a dreadful one {username}
    which do you wish to do, go to battle now
    or postpone the days of evil bearing in mind
    that the longer the days of evil wait the stronger
    they become
    ''')

    print('Pick A to go to battle or pick B to postpne the day of evil: A or B')
    destiny = input('Choose a path: ').upper()

    if destiny == 'A':
        if created_player.health < 500:
            print('''
            your current health stat may be a disadvantage for you in battle
            but you have no choice!, you chose this path.
            ''')
        else:
            print(f'{username} this path is a really tough one')
    
        Ox_Boar = Animal('Ox Boar', randint(30, 50), randint(10, 20), randint(200, 300), randint(10, 30))
        Ox_Boar.print_animal()
        while Ox_Boar.health > 0:
            Ox_Boar.health -= choice(range(1, created_player.attack))
            print(f' Ox Boar {Ox_Boar.health}')
            created_player.health -= choice(range(1, Ox_Boar.attack))
            print(f'Player {created_player.health}')
            if created_player.health <= 0:
                print('Sorry you died, End of game')
                break
        print('You defeated the Ox Boar and some items got dropped')
        print('Ox Boar dropped Health potion')

        health_potion = 150

        print(f'''
         ha ha ha!, {username}, that battle is little compared 
         to what is to come upon you ha ha ha!
         ''')

        Monster_Bear = Monster('Monster_Bear', randint(30, 50), randint(10, 20), randint(200, 300), randint(10, 30), randint(50, 70))
        Monster_Bear.print_monster()
        while Monster_Bear.health > 0:
            Monster_Bear.health -= choice(range(1, created_player.attack))
            print(f' Ox Boar {Monster_Bear.health}')
            created_player.health -= choice(range(1, Monster_Bear.attack))
            created_player.health -= choice(range(1, Monster_Bear.magic))
            if created_player.health < Monster_Bear.health:
                created_player.health += health_potion
            print(f'Player {created_player.health}')
            if created_player.health <= 0:
                print('Sorry you died, End of game')
                break
        print('You defeated the Monster Bear and no items got dropped')

        print(f'''
                ha ha ha! {username}
                you are enetering the dungeon of 
                goblins, this path is dangerous
                if you eventually succeed this path
                a great reward awaits you. you may wish to 
                skip this path if you like
                ''')
        print('Pick A to enter the goblin dungeon or Pick B to continue your journey: A or B')
        decision = input('Choose a path: ').upper()

        if decision == 'A':
            print(f'{username} you have decided to enter the dungeon')

            Goblin_1 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
            Goblin_2 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
            Goblin_3 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
            Goblin_4 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
            Goblin_5 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
            Goblin_6 = Monster('Goblin', randint(5, 10), randint(5, 10), randint(10, 20), randint(5, 10), randint(5, 10))
            Goblin_1.print_monster_goblin()

            while Goblin_1.health and Goblin_2.health and Goblin_3.health and Goblin_4.health and Goblin_5.health and Goblin_6.health > 0:
                Goblin_1.health -= choice(range(1, created_player.attack))
                print(f'{Goblin_1.health}')
                created_player.health -= choice(range(1, Goblin_1.attack))
                Goblin_2.health -= choice(range(1, created_player.attack))
                print(f'{Goblin_2.health}')
                created_player.health -= choice(range(1, Goblin_2.attack))
                Goblin_3.health -= choice(range(1, created_player.attack))
                print(f'{Goblin_3.health}')
                created_player.health -= choice(range(1, Goblin_3.attack))
                Goblin_4.health -= choice(range(1, created_player.attack))
                print(f'{Goblin_4.health}')
                created_player.health -= choice(range(1, Goblin_4.attack))
                Goblin_5.health -= choice(range(1, created_player.attack))
                print(f'{Goblin_5.health}')
                created_player.health -= choice(range(1, Goblin_5.attack))
                Goblin_6.health -= choice(range(1, created_player.attack))
                print(f'{Goblin_6.health}')
                created_player.health -= choice(range(1, Goblin_6.attack))
                if created_player.health < Goblin_1.health + Goblin_2.health + Goblin_3.health + Goblin_4.health + Goblin_5.health + Goblin_6.health:
                    created_player.health += health_potion
                print(f'Player {created_player.health}')
                if created_player.health <= 0:
                    print('Sorry you died, End of game')
                    break
            print('You defeated the Goblins and no items got dropped')

        elif decision == 'B':
            print(f''' {username}, you have decided not to 
                    enter the dungeon by this you have missed the great reward 
                    and you have only made your journey harder
            ''')
    elif destiny == 'B':
        print(f'{username}, you have decided to postpone the day of evil')

else:
    print('You have a chosen the path of darkness and you fell to HELL')
    print(
        '''
        GAME
        OVER
        '''
    )
