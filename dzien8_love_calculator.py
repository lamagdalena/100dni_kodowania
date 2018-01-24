def love_calculator():
    name1 = input('Name number 1:')
    name2 = input('Name number 2:')
    name1 = name1.lower()
    name2 = name2.lower()
    points = 0
    vowels = 'eyuioaóęą'
    consonants = 'qwrtpsdfghjklzxcvbnmśłżźćń'
    vowels_name1 = 0
    vowels_name2 = 0
    consonants_name1 = 0
    consonants_name2 = 0
    
    if name1[0] == name2[0]:
        points += 20
    elif name1[0] in vowels and name2[0] in vowels:
        points += 10
    elif name1[0] in consonants and name2[0] in consonants:
        points += 5
    
    for letter in name1:
        if letter in vowels:
             vowels_name1 += 1
    
    for letter in name2:
        if letter in vowels:
            vowels_name2 += 1
                
    if vowels_name1 == vowels_name2:
        points += 12
        
    for letter in name1:
        if letter in consonants:
            consonants_name1 += 1
            
    for letter in name2:
        if letter in consonants:
            consonants_name2 += 1
            
    if consonants_name1 == consonants_name2:
        points += 12
        
    if ('l' or 'o' or 'v' or 'e' in name1) and ('l' or 'o' or 'v' or 'e' in name2):
        points += 7
        
    love_compatibility = (points / 51) * 100
    
    print('Love compatibility ratio for this couple is:', love_compatibility, '%')
    if love_compatibility >= 80:
        print('You are soulmates!')
    if 80 > love_compatibility >= 50:
        print('It might work...')
    if 50 > love_compatibility > 30:
        print('You are best friends material.')
    if love_compatibility <= 30:
        print('It is a recipe for diasaster!')
