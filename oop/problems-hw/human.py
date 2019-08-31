from pet import Pet


class Human:

    def __init__(self, name="unknown", surname="unknown", year=0, iq=0, pet="unknown", mother='unknown',
                 father='unknown', schedule=None):
        self.__name = name
        self.__surname = surname
        self.__year = int(year)
        if 0 <= iq <= 100:
            self.__iq = iq
        self.__pet = Pet(pet)
        self.__mother = Human(mother)
        self.__father = Human(father)
        if schedule is None:
            schedule = []
        else:
            self.__schedule = list(schedule)

    def greetPet(self):
        print("Hello", self.__pet.nickname)

    def describePet(self):
        print("I have", self.__pet)

    def __str__(self):
        return "name: {}, surname: {}, year: {}, iq: {}, pet: {}. Mother: {}. Father: {}. Schedule: {}".format(
            self.__name,
            self.__surname,
            self.__year,
            self.__iq, 
            self.__pet,
            self.__mother,
            self.__father,
            self.__schedule)
