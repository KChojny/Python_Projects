# Change sign in a game
# Zmiana znaku w grze
def swap(char):
    if char == 'X':
        return 'O'
    else:
        return 'X'


# Compare characters on one line
# Porównanie znaków w jednej linii
def line(ch, ch1, ch2, ch3):
    if ch1 == ch and ch2 == ch and ch3 == ch:
        return True
    else:
        return False


# Try parse string to int
# Próba konwertowania stringu w int
def int_try_parse(value):
    if value.isdigit():
        return True
    else:
        return False


s = '         '
m = [[s[6], s[3], s[0]],
     [s[7], s[4], s[1]],
     [s[8], s[5], s[2]]]
continue_game = 9
sign = 'O'

# Board
# Plansza
#
# Coordinates:
#
# | {1,3} {2,3} {3,3} |
# | {1,2} {2,2} {3,2} |
# | {1,1} {2,1} {3,1} |
#
print(('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------''').format(m[0][2],
                     m[1][2],
                     m[2][2],
                     m[0][1],
                     m[1][1],
                     m[2][1],
                     m[0][0],
                     m[1][0],
                     m[2][0]))

# Loop game
# Pętla z grą
while continue_game:
    print('Now turn {}'.format(swap(sign)))
    a = input('Enter the coordinates: ').split()

    # Checking the number of arguments
    # Sprawdzanie ilości argumentów
    if len(a) != 2:
        print('Write 2 arguments!\n')
        continue

    # Checking types of arguments
    # Sprawdzanie typów argumentów
    if not int_try_parse(a[0]) or not int_try_parse(a[1]):
        print('Write 2 unsigned integers!\n')
        continue

    x = int(a[0]) - 1
    y = int(a[1]) - 1

    # Checking correct coordinates
    # Sprawdzanie poprawnych koordynatów
    if x >= 3 or y >= 3:
        print("Coordinates should be from 1 to 3!\n")
        continue

    # Checking free place on board. Free place is a space in array(' ')
    # Sprawdzanie wolnego miejsca na planszy. Wolne miejsce to spacja w tabeli(' ')
    if m[x][y].isalpha():
        print('This cell is occupied! Choose another one!\n')
        continue

    # Board update
    # Aktualizacja planszy
    sign = swap(sign)
    m[x][y] = sign
    print(('''---------
| {} {} {} |
| {} {} {} |
| {} {} {} |
---------''').format(m[0][2],
                     m[1][2],
                     m[2][2],
                     m[0][1],
                     m[1][1],
                     m[2][1],
                     m[0][0],
                     m[1][0],
                     m[2][0]))
    continue_game -= 1
    wins = []

    # Search for a winning line
    # Szukanie wygrywającej linii
    for i in range(3):
        wins.append(line(sign, m[0][i], m[1][i], m[2][i]))
        wins.append(line(sign, m[i][0], m[i][1], m[i][2]))
    wins.append(line(sign, m[0][0], m[1][1], m[2][2]))
    wins.append(line(sign, m[0][2], m[1][1], m[2][0]))
    winner = any(wins)

    if winner:
        print('{} wins'.format(sign))
        break
    if continue_game == 0:
        print("Draw")
