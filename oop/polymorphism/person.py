class Person:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    # def get_age(self):
    #     return self.__age

    @property
    def age(self):
        return self.__age

    # def set_age(self, age):
    #     if age in range(1, 100):
    #         self.__age = age
    #     else:
    #         print("Invalid age")

    @age.setter
    def age(self, age):
        if age in range(1, 100):
            self.__age = age
        else:
            print("Invalid age")

    # def get_name(self):
    #     return self.__name

    @property
    def name(self):
        return self.__name

    def display_info(self):
        print("Name:", self.__name, "\tAge:", self.__age)

    def __str__(self) -> str:
        return super().__str__()


person = Person("Vlad", 24)
person.display_info()

person.__name = "Vlad111"
person.display_info()

print(person.age)

person.age = 25
print(person.age)

person.display_info()
