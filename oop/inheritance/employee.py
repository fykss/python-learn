# sys.path.insert(
#     0, "/Users/vladyslavlietun/Documents/Projects/Python/Introduction/oop/encapsulation")

from oop.encapsulation.person import Person


class Employee(Person):
    def details(self, company):
        print(self.name, "work in", company)


tom = Employee("Tom", 23)

tom.display_info()
tom.details("Google")

tom.age = 24
tom.display_info()
