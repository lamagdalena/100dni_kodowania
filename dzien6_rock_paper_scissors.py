import random

def one_game():
    choices = ['ROCK', 'PAPER', 'SCISSORS']
    game_number = 0
    you_won = 0
    i_won = 0
    while game_number < 3:
        your_choice = input('ROCK PAPER SCISSORS? (choose one):')
        computers_choice = random.choice(choices)
        print('I choose {}'.format(computers_choice))
        if your_choice.upper() == computers_choice:
            print('You won!')
            you_won += 1
        else:
            print('I won!')
            i_won += 1
        game_number += 1
    print('You won {} times. I won {} times'.format(you_won, i_won))

def one_more_game():
    another_game = input('Do you want to play one more time? (Y/N)')
    if another_game == 'Y' or another_game == 'y':
        rock_paper_scissors()
    elif another_game == 'N' or another_game == 'n':
        print('Thanks for the game!')
    else:
        print('Wrong letter! Try again!')
        one_more_game()
    
def rock_paper_scissors():   
    one_game()
    one_more_game()
