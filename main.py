# this programme calculates how much you would get taxed as an employee, based on your salary

raw = float(input("How much do you earn a year?"))

# national insurance function

def natins(x):
    if raw <= 9568:
        return 0
    elif (raw > 9568) and (raw <= 50270):
        taxed = 0.12*(raw - 9568)
    elif (raw > 50270):
        taxed = 0.12*(50270 - 9568) + 0.02*(raw - 50270)
    else:
        print("Invalid")
    return taxed

# income tax

def inctax(x):
    if raw <= 12570:
        return 0
    elif (raw > 12570) and (raw <= 50270):
        taxed = 0.2*(raw - 12570)
    elif (raw > 50270) and (raw <= 150000):
        taxed = 0.2*(50270 - 12570) + 0.4*(raw - 50270)
    elif (raw > 150000):
        taxed = 0.2*(50270 - 12570) + 0.4*(150000 - 50270) + 0.45*(raw - 150000)
    else:
        print("Invalid")
    return taxed


tax = natins(raw) + inctax(raw)
left = raw - tax
print("You were taxed £" + str(tax) + ".")
print("You have £" + str(left) + " disposable income.")
