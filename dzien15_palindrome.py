def check_if_palindrome():
    word = input('Your word:')
    word = word.lower()
    word_reversed = word[::-1]
    if word_reversed == word:
        return 'Your word {} is a palindrome'.format(word)
    else:
        return 'Your word {} is not a palindrome'.format(word)
