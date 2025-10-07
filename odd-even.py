# Check if a number is odd or even

def check_odd_even():

  number = 7

  remainder = number % 2
  if remainder == 1:
    return True
  else:
    return False

print(check_odd_even())

def check_odd_even():

  number = 7

  remainder = number % 2
  if remainder == 1:
    print("Odd")
  else:
    print("Even")

check_odd_even()