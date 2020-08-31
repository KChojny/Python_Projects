def validation_unsigned_int(value):
    if value.isdigit():
        n = int(value)
        if n >= 0:
            return True
        else:
            return False
    else:
        return False


# Coffee machine status display
# Wyświetlanie stanu w ekspresie
def remaining(array):
    print('''
The coffee machine has:
{} of water
{} of milk
{} of coffee beans
{} of disposable cups
${} of money'''.format(array[0], array[1], array[2], array[3], array[4]))


# Choice and buy coffee
# Wybór i kupowanie kawy
def buy(array):
    # Force the correct command
    # Wymuszanie prawidłowej komendy
    while True:
        print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        num = input()
        if num == 'back':
            return array
        if num is {1, 2, 3}:
            break
        else:
            print('Write valid command!')
            continue

    num = int(num) - 1
    coffee = [[-250, 0, -16, -1, 4],
              [-350, -75, -20, -1, 7],
              [-200, -100, -12, -1, 6]]
    ready = True

    # Checking the quantity in the machine
    # Sprawdzanie ilości w maszynie
    for i in range(4):
        if array[i] + coffee[num][i] <= 0:
            switcher = {
                0: 'water',
                1: 'milk',
                2: 'coffee',
                3: 'cups'
            }
            print('Sorry, not enough {}!'.format(switcher[i]))
            ready = False

    # Updating the quantity of machine components
    # Aktualizacja stanu maszyny
    if ready:
        for i in range(len(coffee[num])):
            array[i] += coffee[num][i]
        print('I have enough resources, making you a coffee!')

    return array


# Add components to coffee machine
# Dodawanie składników do kawy
def fill(array):
    switcher = {
        0: 'ml of water',
        1: 'ml of milk',
        2: 'grams of coffee beans',
        3: 'disposable cups of coffee'
    }
    for i in range(4):
        print('Write how many {} do you want to add:'.format(switcher[i]))
        add = input()
        while not validation_unsigned_int(add):
            print('Write unsigned integer!')
            add = input()
            if validation_unsigned_int(add):
                break
        array[i] += int(add)


# Take money from machine
# Wzięcie piniędzy z maszyny
def take(array):
    print('I gave you ${}'.format(array[4]))
    array[4] = 0


# [water, milk, coffee, cups, money]
# [woda, mleko, kawa, kubki, pieniądze]
# Main program
# Główny program
machine = [400, 540, 120, 9, 550]
print('Write action (buy, fill, take, remaining, exit):')
order = input()
while order != 'exit':
    if order == 'buy':
        buy(machine)

    elif order == 'fill':
        fill(machine)

    elif order == 'take':
        take(machine)

    elif order == 'remaining':
        remaining(machine)

    print('Write action (buy, fill, take, remaining, exit):')
    order = input()
