class Pet:

    def __init__(self, species="undefined", nickname="unknown", age=0, trickLevel=0, habits=None):

        self.__species = species
        self.__nickname = nickname
        self.__age = age
        if 0 <= trickLevel <= 100:
            self.__trickLevel = trickLevel
        if habits is None:
            habits = []
        else:
            self.__habits = list(habits)

    def eat(self):
        print("I'm eating!")

    def respond(self):
        print("Hi host. I -", self.__nickname, "I miss you!")

    def foul(self):
        print("You need to cover the tracks well...")

    @property
    def species(self):
        return self.__species

    @property
    def nickname(self):
        return self.__nickname

    @property
    def age(self):
        return self.__age

    @property
    def trickLevel(self):
        return self.__trickLevel

    @property
    def habits(self):
        return self.__habits

    def __str__(self):
        return "{}[nickname: {}, age: {}, trickLevel: {}, habits: {}].".format(
            self.__species,
            self.__nickname,
            self.__age,
            self.__trickLevel,
            self.__habits)
