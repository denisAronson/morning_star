def count_vowels(word):
    vowels = 0
    for char in word:
        if char in 'aeuioyAEUIOY':
            vowels = vowels + 1

    return vowels

def count_consonants(word):
    consonants = 0
    for char in word:
        if char in 'qzwsxdcrfvtgbhnjmklpQZWSXDCRFVTGBHNJMKLP':
            consonants = consonants + 1

    return consonants

word_x = input('type in any word: ')

word_vowels = count_vowels(word_x)
word_consonants = count_consonants(word_x)

print('consonants -', word_consonants)
print('vowels -', word_vowels)