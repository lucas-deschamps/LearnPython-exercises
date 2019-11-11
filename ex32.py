the_count = [1, 2, 3, 4, 5]
fruits = ['apples', 'oranges', 'pears', 'apricots']
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

print(fruits)

# this first kind of for-loop goes through a list
for numb3r in the_count:
    print(f"This is count {numb3r}")

# same as above
for fruit in fruits:
    print(f"A fruit of type: {fruit}")

# also we can go through mixed lists too
# notice how we have to use {} since we don't know what's in it
for i in change:
    print(f"I got", i(range([change-1])))

# we can also build lists; first start with an empty one
elements = []

# then use the range function to do 0 to 5 counts
for x in range(0, 7):
    print(f"Adding {x} to the list.")
    # append is a function that lists Understand
    elements.append(x)

# random:
# You have two options: Use 0 < x < 10 or 1 <= x < 10, which is classic notation
# or use x in range(1, 10).

# now we can print them out too
for x in elements:
    print(f"Element was: {x}")
