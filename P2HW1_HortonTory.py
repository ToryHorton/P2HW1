
# This program calculates and displays travel expenses

# 4-6-2023

# CTI-110 P2HW1 - Travel

# Tory Horton

#

print("This program calculates and displays travel expenses")

print()

# user enters information

Budget = float(input("Enter Budget: ")) # budget

print()

Location = input("Enter your tavel destination: ") # location

print()

Fuel = float(input("How much do you think you will spend on gas? ")) # fuel

print()

Accomodation = float(input("Approximately, how much will you need for accomodation/hotel? ")) # accomodation

print()

Food = float(input("Last, how much do you need for food? ")) # food

print()

# displays results

print('------------Travel Expenses------------')
print(f'{"Location:":<20}{Location:<10}')
print(f'{"Initial Budget:":<20}${Budget:<10}')
print(f'{"Fuel:":<20}${Fuel:<10}')
print(f'{"Accomodation:":<20}${Accomodation:<10}')
print(f'{"Food:":<20}${Food:<10}')

a = float(int(Budget))
b = float(int(Fuel))
c = float(int(Accomodation))
d = float(int(Food))
balance = a - b - c - d # subtracts expenses to find remaining balance
print('---------------------------------------')

print()

print(f'{"Remaining Balance:":<20}${balance:<10.1f}') # shows remaining balance

print()
