# For the game ill be having different monsters

"""
1. Wolves
2. Werewolves
3. Vampires
4. Devil Bats
5. Monster Bear
6. Monster Dragon
"""
from names import guide, trainer, name


class Monster:
    def __init__(self, type, attack,  health,  magic):
        self.type = type
        self.attack = attack
        self.health = health
        self.magic = magic

    def print_monster_wolf(self):
        print(f"""
        {trainer}:" {name}
        this {self.type}
        has the following stats:
        attack  {self.attack}
        health  {self.health}
        magic  {self.magic}
        
        """)

    def print_monster_motherWolf(self):
        print(f"""
        {trainer}:" {name}
        You have met a mother {self.type}
        resting in her den,  she's hibernating
        but she has stats of :
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_wolfPack(self):
        print(f"""
        {trainer}:" {name}
        You have met a pack of 10 {self.type}
        they each have the following stats:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_werewolf(self):
        print(f"""
        {trainer}:" {name}
        This{self.type}
        has the following stats:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_werewolfPack(self):
        print(f"""
        {trainer}:" {name}
        They are a pack of{self.type}
        they have  the following stats, be careful:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_vampire(self):
        print(f"""
        {trainer}:" {name}
        This{self.type}
        has the following stats:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_3vampires(self):
        print(f"""
        {trainer}:" {name}
        These{self.type}
        have the following stats:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_devilBats(self):
        print(f"""
        {trainer}:" {name}
        These freaking {self.type}
        have the following stats:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_MonsterBears(self):
        print(f"""
        {trainer}:" {name}
        These{self.type}
        have the following stats:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

    def print_monster_MonsterDragon(self):
        print(f"""
        {trainer}:" {name}
        This behemoth {self.type}
        has the following stats:
        attack {self.attack}
        health  {self.health}
        magic  {self.magic}"
        """)

        return Monster
