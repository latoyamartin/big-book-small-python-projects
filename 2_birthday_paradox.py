'''The Birthday Paradox, also called the Birthday Problem, is the surprisingly high probability that two people will have the same birthday even in a small group of people. 
In a group of 70 people, there's a 99.9% chance of two people having the same birthday. But even in a group of just 23 people, there's a 50% chance of two people having the same birthday.
This program performs several probability experiments to determine the percentages for groups of different sizes. We call these types of experiments, in which we conduct multiple random trials
to understand the likely outcomes, Monte Carlo experiments.'''

import datetime
import random
from tracemalloc import start
from urllib import response
from webbrowser import get

def get_birthdays(number_of_birthdays: int):
    """Returns a list of number random date objects for birthdays."""
    birthdays = []
    for i in range(number_of_birthdays):
        # The year is not important for our simulation, as long as all
        # birthdays have the same year.
        start_of_year = datetime.date(2020, 1, 1) # Changed date to 2020 to include the potential for Feb 29 birthdays

        # Get a random day into the year:
        random_number_of_days = datetime.timedelta(random.randint(0, 365)) # Changed to 365 to include the potential for Feb 29 birthdays
        birthday = start_of_year + random_number_of_days
        birthdays.append(birthday)
    return birthdays

def get_match(birthdays: list):
    """Returns the date object of a birthday that occurs more than once in the birthdays list."""
    if len(birthdays) == len(set(birthdays)):
        return None # All birthdays are unique, so return None
    
    # Compare each birthday to every other birthday:
    for a, birthday_a in enumerate(birthdays):
        for b, birthday_b in enumerate(birthdays[a + 1 :]):
            if birthday_a == birthday_b:
                return birthday_a # Return the matching birthday
            
# Display the intro:
print('''The Birthday Paradox shows us that in a group of N people, the odds that two of them have matching birthdays is surprisingly large.
      This program does a Monte Carlo simulation (that is, repeated random simulations) to explore this concept.

      (It's not actually a paradox, it's just a surprising result.)''')

# Set up a tuple of month names in order:
MONTHS = ("Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", 'Dec')

while True: # Keep asking until the user enters a valid amount.
    print("How many birthdays shall I generate? (Max 100)")
    response = input("> ")
    if response.isdecimal() and (0 < int(response) <= 100):
        num_bdays = int(response)
        break # User has entered a valid amount
print()

# Generate and display the birthdays:
print(f"Here are {num_bdays} birthdays:")
birthdays = get_birthdays(num_bdays)
for i, birthday in enumerate(birthdays):
    if i != 0:
        print(", ", end="")
    month_name = MONTHS[birthday.month - 1]
    date_text = f"{month_name} {birthday.day}"
    print(date_text, end="")
print()
print()

# Determine if there are two birthdays that match.
match = get_match(birthdays)

# Display the results:
print("In this simulation, ", end="")
if match != None:
    month_name = MONTHS[match.month - 1]
    date_text = f"{month_name} {match.day}"
    print(f"multiple people have a birthday on {date_text}.")
else:
    print("there are no matching birthdays.")
print()

# Run through 100,000 simulations:
print(f"Generating {num_bdays} random birthdays 100,000 times...")
input("Press Enter to begin...")

print("Let's run another 100,000 simulations.")
sim_match = 0 # How many simulations had matching birthdays in them.
for i in range(100000):
    # Report on the progress every 10,000 simulations:
    if i % 10000 == 0:
        print(f"On simulation {i} of 100,000...")
    birthdays = get_birthdays(num_bdays)
    if get_match(birthdays) != None:
        sim_match = sim_match + 1
print("100,000 simulations run.")

# Display simulation results:
probability = round(sim_match / 100000 * 100, 2)
print(f"Out of 100,000 simulations of {num_bdays} people, there was a matching birthday in that group {sim_match} times. This means that {num_bdays} people have a {probability}% chance of having a matching birthday in their group.")
