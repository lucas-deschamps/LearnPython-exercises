def add(a, b):
    print(f"\nAdding {a} + {b}")
    return a + b

def subtract(a, b):
    print(f"Subtracting {a} - {b}")
    return a - b

def multiply(a, b):
    print(f"Multiplying {a} * {b}")
    return a * b

def divide(a, b):
    print(f"Dividing {a} / {b}")
    return a / b

age = add(20, 5)
height = subtract(185, 10)
weight = multiply(85, 2)
iq = divide(200, 2)

print(f'''\nAge: {age} years old.
Height: {height}cm.
Weight: {weight} pounds.
IQ: {iq} points.\n''')

# Here's a little puzzle:

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
# Variáveis já definidas.
# IQ / 2 = (100 / 2).
# multiply = (170 * 50).
# subtract = (175 - 8500).
# add = (25 + -8325).
# Fórmula: (25+(175-(170*(100/2)))) : (a+(b-(c*(d/2))))
#          (25 + 175 - 170 * 100 / 2)
print("That becomes: ", what, "\nCan you do it by hand?")

# Study drills:
# Once you have the formula worked out for the puzzle,
# get in there and see what happens when you modify the parts of the functions.
# Try to change it on purpose to make another value.
#
# Do the inverse.
# Write a simple formula and use the functions in the same way to calculate it.

def formula(a, b, c, d):
    return (a+(b-(c*(d/2))))

exercise = formula(25, 175, 170, 100)
print(f"Nailed it: {exercise}")

diy = formula(int(input('> ')),
int(input('> ')),
int(input('> ')),
int(input('> ')))
print(f"Your math: {diy}")
