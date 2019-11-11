# When you are doing this kind of specialization, there are three ways that the parent and child classes can interact:

#    Actions on the child imply an action on the parent.
#    Actions on the child override the action on the parent.
#    Actions on the child alter the action on the parent.

### Implicit Inheritance ###

print('### Implicit Inheritance ###')

class Parent(object):

    def implicit(self):
        print("PARENT implicit()")

class Child(Parent):
    pass

dad = Parent()
son = Child()

dad.implicit()
son.implicit()

# The use of pass under the class Child: is how you tell Python that you want an empty block.
# This creates a class named Child but says that there's nothing new to define in it.
# Instead it will inherit all of its behavior from Parent.

# This shows you that if you put functions in a base class (i.e., Parent), then all subclasses (i.e., Child) will automatically get those features.
# Very handy for repetitive code you need in many classes.

### Override Explicitly ###

print('### Override Explicitly ###')

class Parent(object):

    def override(self):
        print("PARENT override()")

class Child(Parent):

    def override(self):
        print("CHILD override()")

dad = Parent()
son = Child()

dad.override()
son.override()

# As you can see, when line 14 runs, it runs the Parent.override function because that variable (dad) is a Parent.
# But when line 15 runs, it prints out the Child.override messages because son is an instance of Child and Child overrides that function by defining its own version.

### Alter Before or After ###

print('### Alter Before or After ###')

class Parent(object):

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def altered(self):
        print("CHILD, BEFORE PARENT altered()")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.altered()
son.altered()

# Because I've overridden Parent.altered the Child.altered version runs, and line 9 executes like you'd expect.
# In this case I want to do a before and after, so after line 9 I want to use super to get the Parent.altered version.
## On line 10 I call super(Child, self).altered(), which is aware of inheritance and will get the Parent class for you.
## You should be able to read this as "call super with arguments Child and self, then call the function altered on whatever it returns."
# At this point, the Parent.altered version of the function runs, and that prints out the Parent message.
# Finally, this returns from the Parent.altered, and the Child.altered function continues to print out the after message.

### Multiple Inheritance ###

# Python has to look-up the possible function in the class hierarchy for both Child and BadStuff, but it needs to do this in a consistent order.
# To do this Python uses "method resolution order" (MRO) and an algorithm called C3 to get it straight.

# Because the MRO is complex and a well-defined algorithm is used,
# Python can't leave it to you to get the MRO right. Instead,
# Python gives you the super() function, which handles all of this for you in the places that you need the altering type of actions as I did in Child.altered.
# With super() you don't have to worry about getting this right, and Python will find the right function for you.

### Using super() with __init__ ###

print('### Using super() with __init__ ###')

# The most common use of super() is actually in __init__ functions in base classes.
# This is usually the only place where you need to do some things in a child, then complete the initialization in the parent.
# Here's a quick example of doing that in the Child:

class Parent(object):
    def __init__(self):
        print('Parent init()')

class Child(Parent):

    def __init__(self, stuff):
        self.stuff = stuff
        stuff = 'Child init()'
        super(Child, self).__init__()
        print(stuff)

Parent()
Child('ye')

# This is pretty much the same as the Child.altered example above,
# except I'm setting some variables in the __init__ before having the Parent initialize with its Parent.__init__.

### Composition ###

print('### Composition ###')

class Other(object):

    def override(self):
        print("OTHER override()")

    def implicit(self):
        print("OTHER implicit()")

    def altered(self):
        print("OTHER altered()")

class Child(object):

    def __init__(self):
        self.other = Other()

    def implicit(self):
        self.other.implicit()

    def override(self):
        print("CHILD override()")

    def altered(self):
        print("CHILD, before OTHER altered()")
        self.other.altered()
        print("CHILD, after OTHER altered()")

print('son = Child()')
son = Child()
print('Finished.')

son.implicit()
son.override()
son.altered()

# In this code I'm not using the name Parent, since there is not a parent-child is-a relationship.
# This is a has-a relationship, where Child has-a Other that it uses to get its work done.

# You can see that most of the code in Child and Other is the same to accomplish the same thing.
# The only difference is that I had to define a Child.implicit function to do that one action.
# I could then ask myself if I need this Other to be a class, and could I just make it into a module named other.py?

# Answer: you could easily make another file (module) with the functions to import

Other.override('ya')

