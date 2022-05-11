from functions import *

P = principal() #Principal amount
r = interest_rate() #Annual interest rate as a decimal
n = 1 #Number of compounding periods per unit of time
t = time() #Time in years


A = P * ((1 + (r/n)) ** (n * t))
interest = r * 100

print(f'£{P} invested at an interest rate of {interest}% for {t} years would be worth £{A}.')

