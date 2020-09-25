from sys import argv
from math import ceil, log, pow


def detector_of_type(string):
    if "." in string:
        return float(string)
    else:
        return int(string)


def annuity(args):
    interest = detector_of_type(args['--interest'])
    i = (interest / 100) / (12 * 1)
    if '--periods' not in args:
        principal = detector_of_type(args['--principal'])
        payment = detector_of_type(args['--payment'])
        periods = ceil(log(payment / (payment - i * principal), i + 1))

        years = periods // 12
        months = periods % 12

        years_word = str(years) + ' year' if years == 1 else str(years) + ' years'
        months_word = str(months) + ' month' if months == 1 else str(months) + ' months'
        years_word = '' if years == 0 else years_word
        months_word = '' if months == 0 else months_word
        and_word = ' and ' if months > 0 and years > 0 else ''

        print(f'It will take {years_word}{and_word}{months_word} to repay this loan!')
        print(f'Overpayment = {(periods * payment) - principal}')

    elif '--principal' not in args:
        payment = detector_of_type(args['--payment'])
        periods = detector_of_type(args['--periods'])

        principal = round(payment / ((pow(1 + i, periods) * i) / (pow(1 + i, periods) - 1)))

        print(f'Your loan principal = {principal}!')
        print(f'Overpayment = {(periods * payment) - principal}')

    elif '--payment' not in args:
        principal = detector_of_type(args['--principal'])
        periods = detector_of_type(args['--periods'])
        payment = ceil(principal * ((pow(1 + i, periods) * i) / (pow(1 + i, periods) - 1)))
        print(f'Your annuity payment = {payment}!')
        print(f'Overpayment = {(periods * payment) - principal}')


def diff(args):
    principal = payment = detector_of_type(args['--principal'])
    periods = detector_of_type(args['--periods'])
    interest = detector_of_type(args['--interest'])
    ii = (interest / 100) / (12 * 1)

    for i in range(periods):
        month_payment = ceil((principal / periods) + ii * (principal - (principal * i / periods)))
        print(f'Month {i + 1}: payment is {month_payment}')
        payment -= month_payment

    print()
    print(f'Overpayment = {-payment}')


values = argv[1:]
dict_args = dict()
error_flag = False
for arg in values:
    args = arg.split('=')
    if len(args) == 2:
        dict_args[args[0]] = args[1]
    else:
        dict_args[args[0]] = ''

numbers = [detector_of_type(dict_args[x]) for x in dict_args if x != '--type']
negative_numbers = []
for x in numbers:
    negative_numbers.append(True if x < 0 else False)

if len(dict_args) == 4 and '' not in dict_args and '--type' in dict_args and not any(negative_numbers):
    if dict_args['--type'] == 'annuity':
        del dict_args['--type']
        annuity(dict_args)
    elif dict_args['--type'] == 'diff' and '--payment' not in dict_args:
        del dict_args['--type']
        diff(dict_args)
    else:
        error_flag = True
else:
    error_flag = True

if error_flag:
    print('Incorrect parameters')
