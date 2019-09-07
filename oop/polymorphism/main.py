from person import Person


class Student(Person):

    def __init__(self, name, age, university):
        super().__init__(name, age)
        self.__university = university

    def display_info(self):
        super().display_info()
        print("University: ", self.__university)

    def __str__(self):
        return "University: {}".format(self.__university)


student = Student("Vlad", 23, "KNU")

student.display_info()

print(student)
