'''
This is a guessing game developed by Ademola
during a bootcamp held by BuggyBillions and
GDSC LAUTECH Ogbomoso.

'''

# To import Random library
import random 
'''
From the random library calling in randint to randomly
choose numbers between 1 and 10
'''

number_to_guess = random.randint(1,10)

# The trial attempt for the user is 3
attempts = 3

'''
While loop begins with the condition being that 
the loop will run as long as the attempt is greater 
than 0
'''
while attempts > 0:

    # User input 
    user_guess = int(input("guess the number between 1-10: "))
    # If user guess is equals to the random number chosen
    if  user_guess != number_to_guess:
        print('your guess is incorrect')

        #deducts the number of attempts by 1
        attempts = attempts - 1

        # to display a warning when the user guess is not equals to the random number chosen and trials is remaining 1 
    if attempts == 1 and user_guess != number_to_guess:
        print('you have 1 more tirals')

        '''
        Its important to let the user know here that
        he dosent have any more trials if at this point
        user guess is not equals to random number chosen.
        Also, the correct answer must be shown. 
        '''
    if attempts == 0 and user_guess != number_to_guess:
        print(f'you have 0 trials and the correct answer is {number_to_guess}')

        '''
        But if the user finally  guesses the correct random
        tell user that his guess is correct and break out 
        of the loop.

        '''
    if user_guess == number_to_guess:
        print('your guess is correct')
        break
        
