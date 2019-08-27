class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = 1

    def set_age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Invalid age")

    def get_age(self):
        return self.__age

    def get_name(self):
        return self.__name

    def display_info(self):
        print("Name:", self.__name, "\tAge:", self.__age)