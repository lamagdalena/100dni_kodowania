import json
import random

def haiku_generator():
    
    def syllables(word):
    #referred from stackoverflow.com/questions/14541303/count-the-number-of-syllables-in-a-word
        count = 0
        vowels = 'aeiouy'
        word = word.lower()
        if word[0] in vowels:
            count +=1
        for index in range(1,len(word)):
            if word[index] in vowels and word[index-1] not in vowels:
                count +=1
        if word.endswith('e'):
            count -= 1
        if word.endswith('le'):
            count+=1
        if count == 0:
            count +=1
        return count

    # inside tekst.txt you can put any text you want
    filename = "tekst_json.json"
    plik = open("tekst.txt")
    zawartosc = plik.read()
    with open(filename, "w") as fp:
        json.dump(zawartosc, fp)
    plik.close()
    with open(filename, "r") as fp:
        tekst_w_json = json.load(fp)
    slowa = tekst_w_json.replace('?', ' ').replace('!', ' ').replace('. ', ' ').replace(',', ' ').replace('-', ' ').split()
    cyfry = '0123456789'

    for cyfra in cyfry:
        for word in slowa:
            if cyfra in word:
                slowa.remove(word)

    number_of_syllables = 0
    one_syllab_word = []
    two_syllab_word = []
    three_syllab_word = []
    four_syllab_word = []
    five_syllab_word = []
    six_syllab_word = []
    seven_syllab_word = []
    more_than_7_syllab_word = []

    for word in slowa:
        number_of_syllables = syllables(word)
        if number_of_syllables == 1:
            one_syllab_word.append(word)
        elif number_of_syllables == 2:
            two_syllab_word.append(word)
        elif number_of_syllables == 3:
            three_syllab_word.append(word)
        elif number_of_syllables == 4:
            four_syllab_word.append(word)
        elif number_of_syllables == 5:
            five_syllab_word.append(word)
        elif number_of_syllables == 6:
            six_syllab_word.append(word)
        elif number_of_syllables == 7:
            seven_syllab_word.append(word)
        else:
            more_than_7_syllab_word.append(word)

    # I used only some of the possible combinations in five and seven_syllab_haiku
    """five_syllab_haiku = random.choice([random.choice(one_syllab_word) + ' ' + random.choice(four_syllab_word), \
                                       random.choice(two_syllab_word) + ' ' + random.choice(three_syllab_word), \
                                       random.choice(five_syllab_word), \
                                       random.choice(one_syllab_word) + ' ' + random.choice(two_syllab_word) + ' ' + random.choice(two_syllab_word)])
    seven_syllab_haiku = random.choice([random.choice(one_syllab_word) + ' ' + random.choice(six_syllab_word), \
                                        random.choice(two_syllab_word) + ' ' + random.choice(five_syllab_word), \
                                        random.choice(three_syllab_word) + ' ' + random.choice(four_syllab_word), \
                                        random.choice(one_syllab_word) + ' ' + random.choice(two_syllab_word) + ' ' + random.choice(four_syllab_word)])
    """
    # we can presume that in every text there will be at least some one and two-syllable words
    one_syllab_word = random.choice(one_syllab_word)
    two_syllab_word = random.choice(two_syllab_word)

    #I used only some of the posiible combinations in completing variables if their lists are empty
    if len(three_syllab_word) > 1:
        three_syllab_word = random.choice(three_syllab_word)
    else:
        three_syllab_word = one_syllab_word + ' ' + two_syllab_word

    if len(four_syllab_word) > 1:
        four_syllab_word = random.choice(four_syllab_word)
    else:
        four_syllab_word = one_syllab_word + ' ' + three_syllab_word

    if len(five_syllab_word) > 1:
        five_syllab_word = random.choice(five_syllab_word)
    else:
        five_syllab_word = one_syllab_word + ' ' + four_syllab_word

    if len(six_syllab_word) > 1:
        six_syllab_word = random.choice(six_syllab_word)
    else:
        six_syllab_word = two_syllab_word + ' ' + four_syllab_word

    if len(seven_syllab_word) > 1:
        seven_syllab_word = random.choice(seven_syllab_word)
    else:
        seven_syllab_word = two_syllab_word + ' ' + five_syllab_word

    five_syllab_haiku = random.choice([one_syllab_word + ' ' + four_syllab_word, \
                                       two_syllab_word + ' ' + three_syllab_word, \
                                       five_syllab_word, \
                                       one_syllab_word + ' ' + two_syllab_word + ' ' + two_syllab_word])
    seven_syllab_haiku = random.choice([one_syllab_word + ' ' + six_syllab_word, \
                                        two_syllab_word + ' ' + five_syllab_word, \
                                        three_syllab_word + ' ' + four_syllab_word, \
                                        one_syllab_word + ' ' + two_syllab_word + ' ' + four_syllab_word])
    another_five_syllab_haiku = random.choice([one_syllab_word + ' ' + four_syllab_word, \
                                       two_syllab_word + ' ' + three_syllab_word, \
                                       five_syllab_word, \
                                       one_syllab_word + ' ' + two_syllab_word + ' ' + two_syllab_word])
    
    print(five_syllab_haiku)
    print(seven_syllab_haiku)
    print(another_five_syllab_haiku)
