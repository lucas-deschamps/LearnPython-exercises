from sys import argv

# don't forget to type some shit in the terminal for filename = argv
print("--------------")
print("How old are you?", end=' ')
age = input()
print("How tall are you?", end=' ')
height = input()
print("How much do you weigh?", end=' ')
weight = input()

print(f"So, you're {age} old, {height} tall and {weight} heavy.")

print("--------------")

script, filename = argv

txt = open(filename)

print(f"Here's your file {filename}:")
print(txt.read())

print("Type the filename again:")
file_again = input("> ")

txt_again = open(file_again)

print(txt_again.read())

print("--------------")

print('Let\'s practice everything.')
print("--------------")
print("You\'d need to know \'bout escapes",
"with \\ that do \\n \nnewlines and \\t \ttabs.")

poem = """
\nThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\t\t\twhere there is none.
"""

print("--------------")
print(poem)
print("--------------")


five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def basic_print_function():
    print("You don't need an arg.")

basic_print_function()
print("--------------")

def secret_formula(started):
    jelly_beans = started * 500
    jarz = jelly_beans / 1000
    cratez = jarz / 100
    print(jelly_beans, jarz, cratez)
    return int(jelly_beans), int(jarz), int(cratez)

start_point = 10000
value1, value2, value3 = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
# it's just like with an f"" string
print(f"We'd have {value1} beans, {value2} jars, and {value3} crates.")

secret_formula(1)

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))

print("--------------")

people = 20
cats = 30
dogs = 15

if people < cats:
    print("Too many cats! The world is doomed!")

if people > cats:
    print("Not many cats! The world is saved!")

if people < dogs:
    print("The world is drooled on!")

if people > dogs:
    print("The world is dry!")

dogs += 5

if people >= dogs:
    print("People are greater than or equal to dogs.")

if people <= dogs:
    print("People are less than or equal to dogs.")

if people == dogs:
    print("People are dogs.")

print("--------------")
