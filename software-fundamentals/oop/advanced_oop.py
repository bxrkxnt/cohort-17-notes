"""
Class method: A method bound to the class - it doesn't need to be a part of an instance
    - A factory method: creates instances of objects

Static method: Bound to the class, similar to a class method
    - Standalone methods (`datetime.now()`)
    - Utility function

Abstract class: A class that is not instantiated, but used to define other classes
    - A base class
    - Guarentees that all subclasses contains the methods inside of it
"""
from datetime import datetime, timedelta
from abc import ABC, abstractmethod, abstractclassmethod

class Animal(ABC):
    def __init__(self, name, age):
        if not isinstance(age, int):
            raise TypeError("Age is not a number!")
        self.name = name
        self.age = age

    def breathe(self):
        print("I am breathing")

    @abstractmethod
    def make_sound(self):
        pass

class Food(ABC):
    def __init__(self, name):
        self.name = name
    
    @staticmethod
    def from_string(food_string: str):
        name, food_type = food_string.split(",")
        if food_type == "Burger":
            return Burger(name)
        pass

class Burger(Food):
    def __init__(self, name):
        super().__init__(name)
class Person(Animal):
    species = "Homo Sapien"

    def __init__(self, name: str, age: int):
        super().__init__(name, age)
        print(f"I, {name}, have been made! My age is now {age}. Behold me and weep!")


    @classmethod
    def from_birth_year(cls, name: str, birth_year: int):
        return cls(name, datetime.today().year - birth_year)
    
    @classmethod
    def from_first_and_surname(cls, first_name: str, surname: str, age: int):
        return cls(" ".join([first_name, surname]), age)
    
    @staticmethod
    def is_adult(age):
        return age > 18
    
    @classmethod
    def reset_age(cls):
        cls.species = "No"

    def make_sound(self):
        print("All shall love me and despair!")

class Goblin(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)
    
    def make_sound(self):
        print("Gooblie Gobbly")
class Baby(Person):
    def __init__(self, name, age):
        super().__init__(name, 2)

    @classmethod
    def from_birth_year(cls, name):
        return super().from_birth_year(name, datetime.today().year)
    
    def make_sound(self):
        print("WAAAAAAAAHHHH!!!!!!")
    
class DateStuff:
    @staticmethod
    def yesterday():
        return datetime.today() - timedelta(days=1)
    
if __name__ == "__main__":
    merino = Person("Merino", 22)
    lando = Person.from_birth_year("Lando", 1992)
    print(lando.is_adult(33))

    print(Person.is_adult(17))

    print(DateStuff.yesterday())

    babes = Baby.from_birth_year("Falooola")

    print(babes.species)

    Person.reset_age()

    print(lando.species)
    print(merino.age)
    merino.breathe()
    # gobbles = Goblin("Svalberd", "Not an age")
    # Say the user is TERRIBLE and we HATE them
    # unpredictable_name = input("Give me a name pls: ")
    # age = input("Gib age pls: ")

    # if " " in unpredictable_name:
    #     if age > 1000:
    #         Person.from_birth_year(unpredictable_name, age)
    #     else: 
    #         first, second = unpredictable_name.split(maxsplit=1)
    #         new_person = Person.from_first_and_surname(first, second, age)