# In this exercise we will cover one more input method you can use to pass variables to a script
# (script being another name for your .py files).
# You know how you type python3.6 ex13.py to run the ex13.py file?
# Well the ex13.py part of the command is called an "argument."
# What we'll do now is write a script that also accepts arguments.

from sys import argv
# read the WYSS section for how to run this
apple, first, second, third = argv
# Line 3 "unpacks" argv so that, rather than holding all the arguments,
# it gets assigned to four variables you can work with: script (mine: apple), first, second, and third.


print("The script is called:", apple)
# sai o nome do script porque ex13.py é um dos arguments quando você dá run
# os outros são os que vem após ex13.py e tomam o lugar das variáveis 1st, 2nd, 3rd
first = input("Input your first variable here: ")
print("Your second variable is:", second)
print("Your third variable is:", third)

print(f"Print the stuff: {apple}, {first}, {second}, {third}.")
