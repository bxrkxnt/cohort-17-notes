from datetime import datetime
from random import randint

def is_it_the_weekend():
    d = datetime.now()
    if d.weekday in (6, 7):
        return True
    return False


def predict_future(question: str) -> str:
    num = randint(0, 2)

    if num == 0:
        return "No"
    elif num == 1:
        return "Yes!!"
    else:
        return "Maybe"




class Horse:

    def __init__(self, name, mane_colour):
        self.name = name # Calling the setter --> self.name(name)
        self.mane_colour = mane_colour
        self._health = 10
        self._max_health = 10

    @property
    def health(self):
        return self._health
    
    @health.setter
    def health(self, val):
        if self._health + val > self._max_health:
            self._health = self._max_health
        else:
            self._health += val

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, new_name):
        if new_name in ["hoofy", "long face"]:
            raise Exception("Anti-horse bigotry")
        self._name = new_name

class Stable:

    def __init__(self, horses: list[Horse]):

        if len(horses) < 3:
            raise ValueError("Stables need at least 3 horses.")

        if not all(isinstance(h, Horse) for h in horses):
            raise TypeError("All horses must, axiomatically, be horses.")

        self.horses = horses


if __name__ == "__main__":

    h = Horse("long face", "golden")
