def piglatin():
    vowels = 'eyuioa'
    pig = 'ay'
    word = input('Write here your word: ')
    if word.isalpha() and len(word) > 0:
        if word[0] in vowels:
            return word + pig
        else:
            for index, letter in enumerate(word):
                if letter in vowels:
                    return word[index:] + word[:(index)] + pig
                    break
