import random


def hangman0():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 11, chr(124))
        elif 4 <= x <= 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))


def hangman1():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 4, chr(124), ' ' * 4, chr(124))
        elif 4 <= x <= 5:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(124), ' ' * 4, chr(124))
        elif x == 6:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(38), ' ' * 4, chr(124))
        elif 7 <= x <= 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))


def hangman2():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 4, chr(124), ' ' * 4, chr(124))
        elif x == 4:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(124), ' ' * 4, chr(124))
        elif x == 5:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(40), chr(95), chr(41), ' ' * 2, chr(124))
        elif x == 6:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(38), ' ' * 4, chr(124))
        elif 7 <= x <= 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))


def hangman3():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 4, chr(124), ' ' * 4, chr(124))
        elif x == 4 or 7 <= x <= 9:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(124), ' ' * 4, chr(124))
        elif x == 5:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(40), chr(95), chr(41), ' ' * 2, chr(124))
        elif x == 6:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(38), ' ' * 4, chr(124))
        elif 10 <= x <= 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))


def hangman4():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 4, chr(124), ' ' * 4, chr(124))
        elif x == 4 or x == 9:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(124), ' ' * 4, chr(124))
        elif x == 5:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(40), chr(95), chr(41), ' ' * 2, chr(124))
        elif x == 6:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(38), ' ' * 4, chr(124))
        elif x == 7:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(47), chr(124), ' ' * 4, chr(124))
        elif x == 8:
            print(chr(124), ' ' * 4, chr(124), ' ' * 3, chr(47), '', chr(124), ' ' * 4, chr(124))
        elif 10 <= x <= 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))


def hangman5():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 4, chr(124), ' ' * 4, chr(124))
        elif x == 4 or x == 9:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(124), ' ' * 4, chr(124))
        elif x == 5:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(40), chr(95), chr(41), ' ' * 2, chr(124))
        elif x == 6:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(38), ' ' * 4, chr(124))
        elif x == 7:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(47), chr(124), chr(92),' ' * 2, chr(124))
        elif x == 8:
            print(chr(124), ' ' * 4, chr(124), ' ' * 3, chr(47), '', chr(124), '', chr(92), ' ', chr(124))
        elif 10 <= x <= 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))


def hangman6():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 4, chr(124), ' ' * 4, chr(124))
        elif x == 4 or x == 9:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(124), ' ' * 4, chr(124))
        elif x == 5:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(40), chr(95), chr(41), ' ' * 2, chr(124))
        elif x == 6:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(38), ' ' * 4, chr(124))
        elif x == 7:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(47), chr(124), chr(92),' ' * 2, chr(124))
        elif x == 8:
            print(chr(124), ' ' * 4, chr(124), ' ' * 3, chr(47), '', chr(124), '', chr(92), ' ', chr(124))
        elif x == 10:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(47), ' ' * 6, chr(124))
        elif x == 11:
            print(chr(124), ' ' * 4, chr(124), ' ' * 3, chr(47), ' ' * 7, chr(124))
        elif x == 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))


def hangman7():
    for x in range(1, 15):
        if x == 1 or x == 14:
            print(chr(45) * 23)
        elif x == 2:
            print(chr(124), ' ' * 4, chr(95) * 10, ' ' * 4, chr(124))
        elif x == 3:
            print(chr(124), ' ' * 4, chr(124), chr(47), ' ' * 4, chr(124), ' ' * 4, chr(124))
        elif x == 4 or x == 9:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(124), ' ' * 4, chr(124))
        elif x == 5:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(40), chr(95), chr(41), ' ' * 2, chr(124))
        elif x == 6:
            print(chr(124), ' ' * 4, chr(124), ' ' * 6, chr(38), ' ' * 4, chr(124))
        elif x == 7:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(47), chr(124), chr(92),' ' * 2, chr(124))
        elif x == 8:
            print(chr(124), ' ' * 4, chr(124), ' ' * 3, chr(47), '', chr(124), '', chr(92), ' ', chr(124))
        elif x == 10:
            print(chr(124), ' ' * 4, chr(124), ' ' * 4, chr(47), ' ', chr(92), ' ' * 2, chr(124))
        elif x == 11:
            print(chr(124), ' ' * 4, chr(124), ' ' * 3, chr(47), ' ' * 3, chr(92), ' ', chr(124))
        elif x == 12:
            print(chr(124), ' ' * 4, chr(124), ' ' * 13, chr(124))
        elif x == 13:
            print(chr(124), ' ', chr(95) * 2, chr(124), chr(95) * 2, ' ' * 10, chr(124))

            
def hangman_game():
    print('Welcome to the Hangman Game!')
    hangman0()
    word_list = ['fasola', 'kanapka', 'krzesło', 'kaloryfer', 'zegarek', 'lampion', 'schody', 'roleta', 'szminka', 'kontrabas']
    secret_word = random.choice(word_list)
    guesses = 0
    number_of_mistakes_left = 7
    letters_used = []
    print('Secret word:')
    print('_ ' * len(secret_word))
    secret_word_as_list = list(secret_word)
    secret_word_guessed = ['_ ' for x in secret_word_as_list]
    while number_of_mistakes_left > 0:
        print('Guesses:', guesses)
        print('Number of mistakes left:', number_of_mistakes_left)
        print('Letters already used:', letters_used)
        your_guess = input('Guess a letter:')
        if your_guess.lower() in letters_used:
            print('You already guessed that letter!')
        elif your_guess.lower() not in 'qwertyuiopasdfghjklzxcvbnm':
            print('Guess A LETTER!')
        elif len(your_guess) != 1:
            print('Guess ONE LETTER!')
        else:
            for index, item in enumerate(secret_word_as_list):
                if item == your_guess:
                    secret_word_guessed[index] = your_guess
                    
        if secret_word_guessed.count(your_guess) == 0:
            number_of_mistakes_left -= 1
            
        if number_of_mistakes_left == 6:
                hangman1()
        elif number_of_mistakes_left == 5:
                hangman2()
        elif number_of_mistakes_left == 4:
                hangman3()
        elif number_of_mistakes_left == 3:
                hangman4()
        elif number_of_mistakes_left == 2:
                hangman5()
        elif number_of_mistakes_left == 1:
                hangman6()
        elif number_of_mistakes_left == 0:
                hangman7()
                print('You lost!')
                print('Secret word was:', secret_word)
                break
        guesses += 1
        letters_used.append(your_guess)
        print('_____________________________________')
        print('Secret word:', ' '.join(secret_word_guessed))   
        if ''.join(secret_word_guessed) == secret_word:
            print('You won!')
            break
