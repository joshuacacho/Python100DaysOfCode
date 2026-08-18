#NO INHERITANCE

class Animal:
    def __init__(self):
        self.num_eyes = 2

    def breathe(self):
        print("Inhale, exhale.")


class Fish():
    def swim(self):
        print("Moving in water")

# normal way of creating new fish object and accessing its method
nemo = Fish()
nemo.swim()

# INHERITANCE

#now lets say we wanted
    # 1 our fish class want to use the animals breathing method

class Fishies(Animal):

    def __init__(self):
        super().__init__()

    # inherit the usper class breathe method and then add onto it for
        # this FISHIES CLASS
    def breathe(self):
        super().breathe()
        print("From class fishies - doing this under water")

    def swim(self):
        print("From class fishies - Moving in water")

# normal way of creating new fish object and accessing its method
nemos = Fishies()
nemos.breathe()





