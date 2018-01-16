import random

def higher_lower():
    liczba = random.choice(range(1, 101))
    
    for x in range(5):
        guess = input('Choose a number from 1 to 100 :')
        if int(guess) == liczba:
            print('You won!')
            break
        elif int(guess) > liczba:
            print('Lower!')
        elif int(guess) < liczba:
            print('Higher!')
    print('You\'re done guessing!')
