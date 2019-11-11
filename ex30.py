people = 30
cars = 25
trucks = 35

# false or true = true
if cars > people or trucks > people:
    print("We should take the cars.")
elif cars < people:
    print("We should not take the cars.")
# if cars > people and cars < people are both false, then else executes:
else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")
elif trucks < cars:
    print("Maybe we could take the trucks.")
else:
    print("We still can't decide.")


if people > trucks:
    print("Alright, let's just take the trucks.")
# if people > trucks is False, then this else executes:
else:
    print("Fine, let's stay home then.")
