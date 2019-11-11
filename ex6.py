types_of_people = 10
x = f"There are {types_of_people} types of people."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {} {}"

print(joke_evaluation.format(types_of_people, do_not))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

# types_of_people = 10 creates a variable named types_of_people
# and sets it = (equal) to 10.
# You can put that in any string with: {types_of_people}.
# You also see that I have to use a special type of string to "format";
# it's called an "f-string"
# Python also has another kind of formatting using the .format() syntax
# which you see on line 17.
# You'll see me use that sometimes
# when I want to apply a format to an already created string, such as in a loop.
