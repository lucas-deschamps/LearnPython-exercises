print("Let's practice everything.")
print('You\'d need to know \' bout escapes with \\ that do:')
print('\n newlines and \t tabs.')

poem = """
\tThe lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("-------------")
print(poem)
print("-------------")

five = 10 - 2 + 3 - 6
print(f"This should be five: {five}")

def secret_formula(started):
    jelly_beans = started * 500
    jarz = jelly_beans / 1000
    cratez = jarz / 100
    return jelly_beans, jarz, cratez

start_point = 10000
arg1, arg2, arg3 = secret_formula(start_point)

# remember that this is another way to format a string
print("With a starting point of: {}".format(start_point))
print(f"We'd have {arg1} beans, {arg2} jars, and {arg3} crates.")

start_point = start_point / 10

print("We can also do that this way:")
formula = secret_formula(start_point)
# this is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, and {} crates.".format(*formula))
print("We'd have {} beans, {} jars, and {} crates.".format(formula,
                                                           formula,
                                                           formula))
