ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("\nWait, there are not 10 things in that list. Let's fix that.\n")

# splits string into a list @ emptyspaces
stuff = ten_things.split(' ')
# 8 items in the list, but ten_things only needs 4 more
more_stuff = ['Day', 'Night', 'Song', 'Frisbee',
              'Corn', 'Banana', 'Girl', 'Boy']

# while loop only adds enough until 10 by popping items of the other list
while len(stuff) != 10:
    print(stuff)
    print(more_stuff)
    next_one = more_stuff.pop()
    print("Adding: ", next_one)
    stuff.append(next_one)
    print(more_stuff)
    print(f"There are {len(stuff)} items now.")
    print(stuff)
    print('\n')

print("There we go: ", stuff, '\n')

print("Let's do some things with stuff:\n")

print(stuff[1]) # prints item #1 in combined list
print(stuff[-1]) # prints last item in combined list
print(stuff.pop()) # pops last item in the list
print(' '.join(stuff)) # prints list by the way of joining them with empty spcs
print('#'.join(stuff[3:6])) # prints list from item 3 to 5 by the way of '#'
print(stuff, '\n')

        ##Study Drills

# Take each function that is called, and go through the steps for function calls
# to translate them to what Python does.
# For example, more_stuff.pop() is pop(more_stuff).

# Translate these two ways to view the function calls in English.
# For example, more_stuff.pop() reads as, "Call pop on more_stuff."
# Meanwhile, pop(more_stuff) means, "Call pop with argument more_stuff."
# Understand how they are really the same thing.

# Go read about "object-oriented programming" online. Confused?
# I was too. Do not worry.
# You will learn enough to be dangerous, and you can slowly learn more later.
