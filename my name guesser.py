import random
words = ['game', 'friend', 'sunset', 'banana', 'magic',
         'python', 'cloud', 'ocean', 'stone', 'mountain',
         'random', 'school', 'forest', 'energy', 'light', 'game', 'hate', 'hammer', 'rizz',
         'ohio', 'sigma', 'tiktok', 'skibidi']


word = random.choice(words)
word_count = ['_'] * len(word)
attempts = 15

while attempts > 0:
    print(f'\ncurrent word : ' + ' '.join(word_count))
    letter = input('Enter a letter \n').strip().lower()
    if letter in word:
        for i in range(len(word)):
            if letter == word[i]:
                word_count[i] = letter
        print('good guess\n')
    else:
        print('loser\n')
        attempts -= 1
    print(f'you have {attempts} ATTEMPTS LEFT')

    if '_' not in word_count:
        print(f'winner , you guessed {word}\n')
        break

    if '_' in word_count and attempts == 0:
        print(f'you lost, answer: {word}\n')
