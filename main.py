# this programme calculates how much you would get taxed as an employee
# based on your salary


PRIMARY_THRESHOLD = 9568
UPPER_EARNINGS_LIMIT = 50270
PERSONAL_ALLOWANCE = 12570
BASIC_LIMIT = 50270
HIGHER_LIMIT = 125140

PRIMARY_RATE = 0.12
UPPER_EARNINGS_RATE = 0.02
BASIC_RATE = 0.2
HIGHER_RATE = 0.4
ADDITIONAL_RATE = 0.45


# receiving user input

def pre_tax():
    entered = input("How much do you earn a year?")

    num_num = 0
    entered_as_decimal = 0

    # check if all characters in the input are numbers or a decimal
    # and that only one decimal is entered, given to two decimal places
    for character in entered:
        if (character == "0") or (character == "1") or \
                (character == "2") or (character == "3") or \
                (character == "4") or (character == "5") or \
                (character == "6") or (character == "7") or \
                (character == "8") or (character == "9") or \
                (character == "." and entered.index(character) != (len(entered) - 1) and entered.index(character) != 0):
            num_num += 1

    if "." in entered:
        if entered.index(".") != entered.index(entered[-3]):
            pre_tax()

    if len(entered) == num_num:
        entered_as_decimal = float(entered)

    else:
        pre_tax()

    return entered_as_decimal


# national insurance function

def natins(x):
    if x <= PRIMARY_THRESHOLD:
        taxed = 0

    elif (x > PRIMARY_THRESHOLD) and (x <= UPPER_EARNINGS_LIMIT):
        taxed = PRIMARY_RATE*(x - PRIMARY_THRESHOLD)

    else:
        taxed = PRIMARY_RATE*(UPPER_EARNINGS_LIMIT - PRIMARY_THRESHOLD)\
                + UPPER_EARNINGS_RATE*(x - UPPER_EARNINGS_LIMIT)

    return taxed

# income tax function


def inctax(x):
    if x <= PERSONAL_ALLOWANCE:
        taxed = 0

    elif (x > PERSONAL_ALLOWANCE) and (x <= BASIC_LIMIT):
        taxed = BASIC_RATE*(x - PERSONAL_ALLOWANCE)

    elif (x > BASIC_LIMIT) and (x <= HIGHER_LIMIT):
        taxed = BASIC_RATE*(BASIC_LIMIT - PERSONAL_ALLOWANCE)\
                + HIGHER_RATE*(x - BASIC_LIMIT)

    else:
        taxed = BASIC_RATE*(BASIC_LIMIT - PERSONAL_ALLOWANCE)\
                + HIGHER_RATE*(HIGHER_LIMIT - BASIC_LIMIT)\
                + ADDITIONAL_RATE*(x - HIGHER_LIMIT)

    return taxed


# function to print taxed amount to two decimal places
def print_tax(x):
    if "." in str(x):
        # when the last digit only occurs once in the sum
        placeholder = str(x)[0:str(x).index(".") + 3]
        x = float(placeholder)

    if str(x).index(str(x)[-1]) == str(x).index(".") + 1:
        print("You were taxed £" + str(x) + "0" + ".")

    else:
        print("You were taxed £" + str(x) + ".")

    return 0

# function to print disposable income amount to two decimal places


def print_left(x):
    if "." in str(x):
        # when the last digit only occurs once in the sum
        placeholder = str(x)[0:str(x).index(".") + 3]
        x = float(placeholder)

    if str(x).index(str(x)[-1]) == str(x).index(".") + 1:
        print("You have £" + str(x) + " disposable income.")

    else:
        print("You have £" + str(x) + " disposable income.")

    return 0


# main programme

raw = pre_tax()
tax = natins(raw) + inctax(raw)
left = raw - tax
print_tax(tax)
print_left(left)

