from random import seed, choice
from string import ascii_lowercase

words = ['python', 'java', 'kotlin', 'javascript']

print('H A N G M A N')

while True:
    print()
    command = input('Type "play" to play the game, "exit" to quit: ')
    if command == 'play':
        seed()
        word = choice(words)
        letters = '-' * len(word)
        lives = 8
        d = dict()
        for x in ascii_lowercase:
            d[x] = False

        while lives != 0 and '-' in letters:
            print()
            print(letters)
            letter = input('Input a letter: ')

            if len(letter) != 1:
                print('You should input a single letter')
            elif letter.isupper() or not letter.isalpha():
                print('It is not an ASCII lowercase letter')
            elif d[letter]:
                print("You already typed this letter")
            elif letter not in word:
                print("No such letter in the word")
                d[letter] = True
                lives -= 1
            print(lives)
            if lives == 0:
                break
            else:
                for i in range(len(word)):
                    if letter == word[i]:
                        letters = letters[:i] + letter + letters[i + 1:]
                        d[letter] = True

        if '-' not in letters:
            print(f'''You guessed the word {letters}!
You survived!''')
        elif lives == 0:
            print('''You lost!''')
    elif command == 'exit':
        break
