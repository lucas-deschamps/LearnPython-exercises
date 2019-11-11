## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a attribute named 'name'
        self.name = name
        print(self.name, 'is-a dog.')

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## Cat has-a attribute named 'name'
        self.name = name
        print(self.name, 'is-a cat.')

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## Person has-a attribute named 'name'
        self.name = name
        print('-' * 5)
        print(self.name, 'is-a person.')

        ## Person has-a attribute named 'pet'
        self.pet = None
        print(f'Pet = {self.pet}.')
        print('-' * 5)

class Pet_Person(Person):

    def __init__(self, name, pet):
        self.name = name
        self.pet = pet
        print(f"Pet person is called {self.name}; has {self.pet} pet.")

print('~' * 10)

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        print('\n=========')
        ## ?? hmm what is this strange magic?
        self.name = name

        # What does super(Employee, self).__init__(name) do?
        # That's how you can run the __init__ method of a parent class reliably.
        # super(Employee, self)
        # AttributeError: 'Employee' object has no attribute 'name'
        ## Employee has-a salary of some kind
        self.salary = salary
        print('<Employee start.>')
        print(self.name, 'is-a employee.')
        print(name, '- printed name.')
        print(salary, '- printed salary.')
        print(f'Has-a {self.salary} dollars salary.')
        print(f'{self.name} is-a employee, and has-a {self.salary} dollars salary.')
        print(Employee, '- printed employee class.')
        print(Employee.__init__, '- printed init function.')
        print('<End of employee.>')
        print('=' * 10, '\n')

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


print('<<<Start classes.>>>')

## rover is-a Dog
rover = Dog("Rover")

## satan is-a Cat
satan = Cat("Satan")

print()
Pet_Person("Testo", 'Peto')
print()

## mary is-a Person
mary = Person("Mary")
mary = Pet_Person("Mary", "Luciferrr")
mary = Pet_Person("Maria", "{}".format(mary.pet))

## mary has-a pet satan
mary.pet = "Satan"

mary = Pet_Person("Maria_after_mary.pet=\"Satan\"", "{}".format(mary.pet))
mary = Person("{}".format(mary.pet))

Employee("Mario", 64)
