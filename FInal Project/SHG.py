"""
Welcome to Shadow Garden is an RPG styled game.
Built by Ajadi Ademola. It includes a fascinating
storyline. It's Amazing!
"""

import hashlib
import time
from random import randint, choice
from Monsters import Monster

from names import guide, trainer, name, friend_1, friend_2

print(f""" Welcome to Shadow Garden, we who lurk in the shadows to hunt the shadows.
To have you join us tell me your name I am {guide}
""")

username = input('Enter your name:')

print(f""" I have noticed unique abilities from you {username}, to continue enter your password
""")
print(f""" your username is {username}""")
user_password = input('Enter your  password: ')
confirm_user_password = input('Confirm the password above: ')
time.sleep(8)
# password validation
while user_password != confirm_user_password:
    print('Passwords do not match, enter passwords again')
    # Enter passwords
    user_password = input('Enter a password: ')
    confirm_user_password = input('Confirm the password above: ')
    if user_password == confirm_user_password:
        break
encoded_pass = hashlib.md5(confirm_user_password.encode())


class Player:
    def __init__(self, power):
        self.power = power

    def starting_player_stats(self):
        print(f"""
        {trainer}:"You are just joining us and currently your stats are
        shadow power : {self.power}%
        Magical Ability : 0
        Weapon : none
        Special skill power : none 
        you have to train hard to become slightly as strong as I
        {trainer}(aside)"You'll never become as strong as boss though :)
        """)
        return Player


the_newbie = Player(randint(350, 500))
weapon = []
Magical_Herbs = []

print(f"""
        {guide}:"
        {username}, welcome you are now a member of shadow garden.
        You have been gifted the power of the shadows,magical power.
        I will be assigning you to your trainer {trainer} from here onwards your name shall be
        {name}"
        {guide}:"{trainer} take care of {name}"
        {guide}:"{name} prove to us that you are worthy of the power bestowed upon you"
        {trainer}: "lady{guide}!, that's my line thank you I'll take it from here.
        You must have a lot to attend to since Lord Shadow is currently away in another 
        dimension."
        """)
time.sleep(30)
the_newbie.starting_player_stats()
time.sleep(15)
print(f"""
{trainer}:" {name} lets begin your training.
I'll train you to be among the strongest amongst your friends.
Give your heart and mind to your training so that boss will acknowledge you."
{trainer}:" Lord Shadow is away after being sucked into the black rose, but I know
he will be back so I'll do my best until he comes back."
{trainer}: let's begin {name}
(she carries you away from the training ground)
(wonder where you're going right?)
***
***
***
***
***
""")
time.sleep(20)
print(f"""
(you arrive in a dark forest)
(you're scared?, don't be after all delta is one of the 
strongest amongst the 7 shadows)
{trainer}:" a ha! here we are, I think this is the last 
spot I spotted one of those weaklings, they will be perfect
for a start"
(this is delta's favourite hunting ground)
(all the monsters here have unending beef against her)
(watch out! a wolf is approaching you)
{trainer}:" there! go beat that wolf. make use of the shadow power bestowed on you.
only through battles can you become strong!"
""")
time.sleep(10)

Wolf = Monster('Wolf', randint(0, 70), randint(10, 50), randint(0, 30))
Wolf.print_monster_wolf()

print('you are about to engage in a battle with this monster')
time.sleep(3)
wolfAttack = Wolf.attack + Wolf.magic

while Wolf.health > 0:
    Wolf.health -= choice(range(1, the_newbie.power))
    Wolf.attack -= choice(range(1, the_newbie.power))
    Wolf.magic -= choice(range(1, the_newbie.power))
    print(f' Wolf {Wolf.health}')
    the_newbie.power -= choice(range(1, wolfAttack))
    print(f'{name} {the_newbie.power}')
    if the_newbie.power <= 0:
        print('sorry you died you were weak after all')
        break
    print(f"""{trainer}:"{name}
    ha! ha! you have defeated the wolf weldone.
    the wolf's magic has evolved into this weapon
    the light saber sword!""")
    light_saber_sword = 150
    defeatedWolfPower = 100

    time.sleep(8)
weapon.append('light_saber_sword')
the_newbie.power += defeatedWolfPower


class CurrentPlayer(Player):

    def __init__(self, power):
        self.attack = 150

        Player.__init__(self, power)

    def cr_pl_stat(self, ):
        print(f"""
        your current stats are:
        power: {self.power}
        attack: {self.attack}
        weapon : {weapon}
        """)

        return CurrentPlayer


cr_stats = CurrentPlayer(the_newbie.power)

cr_stats.cr_pl_stat()
time.sleep(7)
print('after then you both return to the shadow garden base')
time.sleep(3)
print(f"""
{trainer}: {name}, you did well today!.
You have also earned a new weapon which has improved your attack skill.
for now go ahead with these two {friend_1} and {friend_2}. I'll be back!
""")
time.sleep(25)
print(f"""
{friend_1}: hello {name} glad to have you I'm {friend_1} by the way.
{friend_2}: Brat! hasn't the lady Delta introduced us before?. Anyways{name}
we were just about to head out.. {friend_1}: wait we've just met {name} do we have to 
go there today?
{friend_2}: are you dumb!, how can you decide to stop training when you're nowhere near the
strength pf the 7 shadows!
{friend_2}: I'll ask you {name} are you willing to go with uus to train right now?
""")
print('are you willing to go?: YES or NO')
hunt = input('YES or NO: ').upper()

if hunt == 'YES':
    print(f"""
    {friend_2}: "A ha! you've got no excuse now {friend_1}
    {name} has agreed and we are going into besiege the wolves den.
    Ha! ha! ha!." 
    {friend_1}: alright, since {name} agrees lets go then.
    """)
    time.sleep(2)
    print("**You've agreed to follow your new friends to hunt!**")
    print("**You've made the right choice!**")
    time.sleep(5)

    print("**You've arrived at the wolves den.**")
    print(f"""
    Wolves: "Grr! Grrr! Awoooo!"
    {friend_2}: This is unexpected!, why are they agitated...i.ts like
    they've been waiting for us to come!
    {friend_1}: I knew this wasn't a good idea lets leave now!
    {friend_2}: Relax {friend_1}. {name} Lady{trainer} took you 
    out to hunt too right?, Did you hunt down a wolf that looks 
    like this pack of wolves?
    """)
    print('is this true?: YES or NO')
    kill = input('YES or NO: ').upper()

    if kill == 'YES':
        print(f"""
        {friend_2}: A ha!, you see {friend_1}, they're not 
        agitated over nothing
        {friend_1}: that explains it.
        """)
    elif kill == 'NO':
        print(f"""
        {friend_2}: Then what could've caused their anger?
        {friend_1}: We don't know that the more reason for us to leave!
        {friend_2}: This is unusual.
        """)
    else:
        print(f"""
        {friend_2}: Never-mind
        """)

    print(f"""
    {friend_2}: Regardless we are staying!. I'm not afraid of
    their useless growling!. Ha! it's just a pack of 10 wolves.
    Let's attack!
    """)
    time.sleep(10)

    print("** You're about to attack the wolves brace yourself!**")
    print(f"**{friend_2} is trying to fight them all alone, you have to help!**")
    print(f"*** look! 4 wolves are running towards you looking savagely!**")
    time.sleep(2)

    Wolf1 = Monster('Wolf', randint(0, 70), randint(10, 50), randint(0, 30))
    Wolf2 = Monster('Wolf', randint(0, 70), randint(10, 50), randint(0, 30))
    Wolf3 = Monster('Wolf', randint(0, 70), randint(10, 50), randint(0, 30))
    Wolf4 = Monster('Wolf', randint(0, 70), randint(10, 50), randint(0, 30))

    Wolf1.print_monster_wolfPack()

    print('you are about to engage in a battle with these monsters')
    wolf1Attack = Wolf1.attack + Wolf1.magic
    wolf2Attack = Wolf1.attack + Wolf2.magic
    wolf3Attack = Wolf1.attack + Wolf3.magic
    wolf4Attack = Wolf1.attack + Wolf4.magic
    nameAttack = cr_stats.attack + cr_stats.power
    while Wolf1.health and Wolf2.health and Wolf3.health and Wolf4.health > 0:
        Wolf1.health -= choice(range(1, nameAttack))
        cr_stats.power -= choice(range(1, wolf1Attack))
        print(f' Wolf: {Wolf1.health}')
        print(f' {name}: {cr_stats.power}')
        Wolf3.health -= choice(range(1, nameAttack))
        cr_stats.power -= choice(range(1, wolf2Attack))
        print(f' Wolf: {Wolf2.health}')
        print(f' {name}: {cr_stats.power}')
        Wolf2.health -= choice(range(1, nameAttack))
        cr_stats.power -= choice(range(1, wolf3Attack))
        print(f' Wolf: {Wolf3.health}')
        print(f' {name}: {cr_stats.power}')
        Wolf4.health -= choice(range(1, nameAttack))
        cr_stats.power -= choice(range(1, wolf4Attack))
        print(f' Wolf: {Wolf4.health}')
        print(f' {name}: {cr_stats.power}')
        if cr_stats.power <= 0:
            print('sorry you died you were weak after all')
            break
    print(f'''You defeated the Wolves and you have gained "Atlas Apple" a 2nd grade Magical Herb
        this will improve your health stats
    ''')
    DefeatedwolvesPower = 400
    DefeatedwolvesHealth = 400
    time.sleep(8)

    Magical_Herbs.append('Atlas Apple')
    Atlas_apple = 200


    class CurrentPLayer2(CurrentPlayer):
        def __init__(self, power, attack, health):
            self.health = Atlas_apple

            CurrentPlayer.__init__(self, power)

        def cr_pl_stat2(self, ):
            print(f"""
            Your Current stats are:
            power: {self.power}
            attack: {self.attack}
            weapon: {weapon}
            health: {self.health}
            Magical Herbs: {Magical_Herbs}           
             """)

            return CurrentPLayer2


    cr_stats2 = CurrentPLayer2(cr_stats.power, cr_stats.attack, Atlas_apple)
    cr_stats2.power += DefeatedwolvesPower
    cr_stats2.health += DefeatedwolvesHealth
    print('Do you wish to check your current stats?: YES or NO')
    stats = input('YES or NO: ').upper()

    if stats == 'YES':
        cr_stats2.cr_pl_stat2()

    else:
        print('****')

    time.sleep(3)
    print("* It seems you have defeated the wolfe pack*")
    time.sleep(2)
    print(f"""
    {friend_2}: Ha! Ha! that was a good fight! But in the end
    the power of the shadows reigns supreme!
    {friend_1}: {name} I hope you're fine. {friend_2} is too 
    reckless.
    {name}: I'm fine thank you.
    {friend_2}: Who knew {name} was as strong as this. You took
    on 4 wolves effortlessly, I'm impressed.
    {friend_1}: Can we please return now?
    {friend_2}: Sure!. {name} it was nice meeting you.
    """)
    time.sleep(5)
    print("*You've returned to the shadow garden base")
    time.sleep(3)

    # print(f"""
    # {trainer}: I caught word that you went to hunt with those two
    # {name}: That is true.
    # {trainer}: I can also see that you have become stronger. This is good.
    # """)

elif hunt == 'NO':
    print("*That was a bad idea you decided to stay doing nothing*")
    print("*The way of the shadow is to train*")
    print("*You have to wait for Lady Delta to be back*")
    time.sleep(3)

print('*There is lady Alpha you should go talk to her*')
time.sleep(2)

print(f"""
{guide}:"How are you {name}, you must be on your own
since {trainer} is away on a important mission. 
""")

if hunt == 'YES':
    print(f"""
    {guide}: I have a important mission for you.
    It seems you're strong enough for this
    """)
    cr_stats2.cr_pl_stat2()
elif hunt == 'NO':
    print(f"""
    {guide}: I have a important mission for you.
    But you don't seem to be strong enough for it.  
    """)
    print(f'{guide}: Your current stats is too low')
    cr_stats.cr_pl_stat()

# To be continued>>>
