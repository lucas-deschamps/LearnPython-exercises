i = 0
# [] makes a list
numbers = []

# ranges start from 0 and end before the last number defined in the range in py
while i < 6:
    print(f"At the top i is {i}")
    numbers.append(i)

    i = i + 1
    # i += 1
    print("Numbers now: ", numbers)
    print(f"At the bottom i is {i}")

    if i == 2:
        print("i is now 2", i)

    elif i == 4:
        print("##numbers is now at##", numbers)

print("The numbers: ")

for nums in numbers:
    print(nums)

## study drill

# Convert this while-loop to a function that you can call,
# and replace 6 in the test (i < 6) with a variable.

def studydrill(first):
    print("\n[Function]: Hi.")
    x = 0
    y = 6
    zordon = 2
    while x < y:
        print(f"At the top x is {x}")
        x = x + zordon
        print(f"At the bottom x is {x}")

studydrill({})

def studydrill(*first):
    print("\n[Goldar]: Hi.")
    x = 0
    y = 6
    goldar = 1
    numberz = []
    while x < y:
        print(f"\nAt the top x is {x}")
        numberz.append(x)
        x = x + goldar
        print(f"At the bottom x is {x}")
        print(numberz)

studydrill()

# Loops are hard. How do I figure them out?

def ezloop(ez):
    print('\nFunction start.')
    x = 0
    while x < 11:
        print(x)
        print('Second part.')
        x = x + 1
        print('Third part.')
        print(x)
        print('Fourth part.')
        print('Function end; looping.')

ezloop(())
