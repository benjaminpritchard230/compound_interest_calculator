def principal():
    """Gets the principal amount."""
    while True:
        while True:
            try:
                P = int(input('Enter the principal amount:\n')) #Principal amount
            except ValueError:
                print('You did not enter an amount.')
                continue
            break
        if P <= 0:
            continue
        else:
            return P


def interest_rate():
    """Gets the interest rate and makes sure that it is a decimal."""
    while True:
        try:
            R = float(input('Enter the annual interest rate as a percentage or decimal:\n')) #Annual interest rate as a decimal
        except ValueError:
            print('You did not enter an amount.')
            continue
        break
    if R >= 1:
        r = R / 100
    else: 
        r = R
    return r
        
def time():
    """Gets the calculation time in years."""
    while True:
        while True:
            try:
                t = int(input('Enter the number of years:\n')) #Time in years
            except ValueError:
                print('You did not enter an amount.')
                continue
            break
        if t <= 0:
            print('Time in years must be a positive number.')
            continue
        else:
            return t


