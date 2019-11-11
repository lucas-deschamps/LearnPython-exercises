# this one is like scripts with argv
def print_two(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

# ok, that args is actually pointless, we can just do this:
def print_two_again(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

# this one takes just one argument
def print_one(arg1):
    print("arg1: {}" .format("Second!"))

def print_one_again(arg1):
    arg1 = "Third!"
    print(f"arg1: {arg1}")

# this one takes no arguments
def print_none():
    print("I got nothin'.")

print_two("John", "Doe")
print_two_again("Zed", "Shaw")
print_one(())
print_one_again(())
print_none()
