class Bee:

    def __init__(self, name, species):
        self.name = name
        self.species = species
        self.legs = 6

    def buzz(self):
        return "BUZZ!"

    def __repr__(self) -> str:  # If this is represented while printing something else
        return f"Bee({self.name})"

    def __str__(self) -> str:  # If we print this directly
        return self.__repr__()


class HoneyBee(Bee):

    def __init__(self, name, hive): # When we make a honeybee
        super().__init__(name, "apis mellifera")  # We also make the bee bit
        self.hive = hive

    def __repr__(self) -> str:
        return f"HoneyBee({self.name})"


if __name__ == "__main__":

    b = Bee("Angela", "mason bee")
    b2 = HoneyBee("Dominic", "Wales")

    print(b)
    print(b2.buzz())
    print(isinstance(b2, HoneyBee))
    print(isinstance(b2, Bee))