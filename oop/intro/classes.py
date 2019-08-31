class Person:

    # constructor
    def __init__(self, name):
        self.name = name

    def displey_info(self):
        print("Hello, my name is", self.name)


class Auto:

    def __init__(self, name):
        self.name = name

    def move(self, speed):
        print(self.name, "rides at a speed", speed, "km/h")
