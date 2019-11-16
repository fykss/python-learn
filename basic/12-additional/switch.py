def switch_case1(argument):
    switcher = {
        0: "zero",
        1: "one",
        2: "two"
    }

    return switcher.get(argument, "nothing")


print(switch_case1(3))


def one():
    return "January"


def two():
    return "February"


def three():
    return "March"


def switch_case2(argument):
    switcher = {
        1: one(),
        2: two(),
        3: three()
    }

    return switcher.get(argument, "nothing")


print(switch_case2(2))
