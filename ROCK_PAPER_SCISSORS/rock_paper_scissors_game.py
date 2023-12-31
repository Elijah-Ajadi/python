from random import choice

print('Welcome to Rock Paper Scissors 1.0 by Ademola :-)')

# defining username and system name
system_name = ('Albatross')
username = input('Please input your desired name player: ')
print(f'I shall call you {username} from now on I am {system_name} by the way.')
print('In this game we will pick cards against eachother, these cards are Rock, Paper and Scissors')

#Albatross properties
class Albatross:
    def __init__(self, items ):
        self.items = items
        
        return Albatross



game = input(f'{username} input your desired game card: ')
user_choice = game

# Score counts for the game
user_count = 0
Albatross_count = 0

# Totaling the game count after each round but will only print at the end
game_count = (Albatross_count + user_count)

''''
# Condition for while loop to contine running
untill the total game count is = 10
'''
while game_count != 10:
    '''
    # using random's choice function to 
    make the system pick randomly between
    rock, paper or scissors. And multiplying
    the number of each item by 9 to futher improve
    randomliness
    
    '''
    items = ['Rock', 'Paper', 'Scissors'] * int(9)
    chosen_item = choice(items)
    Albatross_choice = chosen_item

    # Calling in user's input and defining it as user_choice
    game = input(f'{username} input your desired game card: ')
    user_choice = game

    # Passing in the totaling function again for the while loop
    game_count = (Albatross_count + user_count)


    # using if statments to define the conditions of who wins. they total up to 9 if statments
    if user_choice == 'Rock' and Albatross_choice == 'Rock':
        user_count += 0
        Albatross_count += 0
        print('this round is a draw')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')

    elif user_choice == 'Paper' and Albatross_choice == 'Paper':
        user_count += 0
        Albatross_count += 0
        print('this round is a draw')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')

    elif user_choice == 'Scissors' and Albatross_choice == 'Scissors':
        user_count += 0
        Albatross_count += 0
        print('this round is a draw')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')

    elif user_choice == 'Scissors' and Albatross_choice == 'Rock':
        user_count += 0
        Albatross_count += 1
        print(f'{system_name} wins')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')

    elif user_choice == 'Rock' and Albatross_choice == 'Scissors':
        user_count += 1
        Albatross_count += 0
        print(f'{username} wins')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')

    elif user_choice == 'Scissors' and Albatross_choice == 'Paper':
        user_count += 1
        Albatross_count += 0
        print(f'{username} wins')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')
        
    elif user_choice == 'Paper' and Albatross_choice == 'Scissors':
        user_count += 0
        Albatross_count += 1
        print(f'{system_name} wins')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')

    elif user_choice == 'Rock' and Albatross_choice == 'Paper':
        user_count += 0
        Albatross_count += 1
        print(f'{system_name} wins')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')

    elif user_choice == 'Paper' and Albatross_choice == 'Rock':
        user_count += 1
        Albatross_count += 0
        print(f'{username} wins')
        print(f'the scores are Albatross:{Albatross_count}, {username}:{user_count}')


    # defining the statments to break the loop which activates when game_count == 10 as declared above
    if game_count == 10 and Albatross_count == user_count:
        print(f''''
        That was a nice match {username}. 
        Although you could not beat me,
        the match was a draw and the total score is
        {game_count}''')

    elif game_count == 10 and Albatross_count > user_count:
        print(f'''
        That was a nice match {username}.
        {system_name} beat you tho.
        I won the match and the total score is
        {game_count}
        ''')

    elif game_count == 10 and Albatross_count < user_count:
        print(f'''
        That was a superb one! {username}.
        You have won against {system_name},
        and the total score is
        {game_count}
        ''')

        break
