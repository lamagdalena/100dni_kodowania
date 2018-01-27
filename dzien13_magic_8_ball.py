import random

def magic_8_ball():
    answers =  ['It is certain', 'It is decidedly so', 'Without a doubt', 'Yes definitely', 'You may rely on it', \
                'As I see it, yes', 'Most likely', 'Outlook good', 'Yes', 'Signs point to yes', 'Reply hazy try again', \
                'Ask again later', 'Better not tell you now', 'Cannot predict now', 'Concentrate and ask again', \
                'Dont count on it', 'My reply is no', 'My sources say no', 'Outlook not so good', 'Very doubtful']
    print('I am the MAGIC 8 BALL. Ask me a yes/no question.')
    question = input('What is your question? : ')
    answer = random.choice(answers)
    print(answer)
    continue_play = input('Do you have another question? Choose Y (yes) or N (no).')
    if continue_play in 'Nn':
        return 'OK then. Bye!'
    elif continue_play in 'Yy':
        magic_8_ball()
    else:
        print('I presume then that the answer is no..')
