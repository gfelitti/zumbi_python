## Animal is-a object
class Animal(object):
    pass

#Dog is-a Animal
class Dog(Animal):
    def __init__(self, name):
        ## Dog has-a name
        self.name = name

#Cat is-a Animal
class Cat(Animal):
    def __init__(self, name):
        #Cat has-a name
        self.name = name

## Person is-a object
class Person(object):
    def __init__(self, name):
        ##Person has-a name
        self.name = name
        ##Person has-a pet of some kind
        self.pet = None

#Employer is-a Person
class Employer(Person):
    def __init__(self, name, salary):
        ##:
        super(Employer, self).__init__(name)
        ## Emplyer has-a salary
        self.salary = salary

# Fish is-a object
class Fish(object):
    pass

class Salmon(Fish):
    pass

class Halibut(Fish):
    pass

rover = Dog("Rover")
satan = Cat("Satan")
mary = Person("Mary")
mary.pet = satan
frank = Employer("Frank", 1200000)
frank.pet = rover
flipper = Fish()
crouse = Salmon()
harry = Halibut()
