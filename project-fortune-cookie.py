# Fortune Cookie Project

import random

lucky_number = random.randint(1, 100)

fortune_number = random.randint(1, 3)

lucky_text = ""

if fortune_number == 1:
    lucky_text = "Today is your lucky day!"
elif fortune_number == 2:
    lucky_text = "You will find great success in your endeavors."
else:
    lucky_text = "Happiness is around the corner."

print(f"{lucky_text} Your Lucky Number is: {lucky_number}")
