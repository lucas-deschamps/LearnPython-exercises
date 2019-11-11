from sys import argv

script, input_file = argv

# use currenttest.txt for this

def print_all(f):
    print(">>> print_all: f=", f)
    print(f.read())
    print("<<< print_all: f=", f)

def rewind(f):
    f.seek(0)

def print_a_line(line_count, f):
    print(line_count, f.readline())

current_file = open(input_file)

print("First, let's print the whole file:\n")

print_all(current_file)

print("Now let's rewind - kind of like a tape.")

rewind(current_file)

print("Let's print three lines:")

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

# += is
# property += 1
# the shorthand notation for
# property = property + 1;

current_line = current_line + 1
print_a_line(current_line, current_file)

rewind(current_file)
# not printing four, four, four, four
current_line += 4
print_a_line(current_line, current_file)
