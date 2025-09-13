import random
word_list = ['game', 'hate', 'hammer', 'rizz',
'ohio', 'sigma', 'tiktok', 'skibidi','game', 'friend', 'sunset', 'banana', 'magic', 
'python', 'cloud', 'ocean', 'stone', 'mountain', 
'random', 'school', 'forest', 'energy', 'light'
]
word = random.choice(word_list)
word_guess = ['_'] * len(word)
attempts = 10

while attempts > 0:
    print('\ncurrent word' + ' ' + ' '.join(word_guess))
    guess = input('\nguess a letter\n').lower()
    if guess in word:
        for i in range(len(word)):
            if guess == word[i]:
                word_guess[i] = guess
        print('\ngreat guess!')
    else:
        attempts -= 1
        print(f'\nwrong guess! you have {attempts} attempts')

    if '_' not in word_guess:
        print(f'\ncongrats you guessed the word {word}')
        break
    if '_' in word_guess and attempts == 0:
        print(f'you lost, the word was {word}')
