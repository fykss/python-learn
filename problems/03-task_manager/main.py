active_app = True
schedule = []

schedule.append(["Sunday", "do home work"])
schedule.append(["Monday", "go to courses", "watch a film"])
schedule.append(["Tuesday", "go to gym"])
schedule.append(["Wednesday", "go to university", "read a book"])
schedule.append(["Thursday", "go to swimming pool"])
schedule.append(["Friday", "go to courses"])
schedule.append(["Saturday", "relax", "walk with friend"])


while active_app:
    day = input("Please, input the day of the week: ")
    correct = False
    task = []

    for i in range(len(schedule)):
        if day.lower() == schedule[i][0].lower():
            correct = True
            task = schedule[i][1:]

    if correct:
        print("Your tasks for {day}: {tasks}".format(
            day=day, tasks=", ".join(task)))
    elif day.lower() == "exit":
        active_app = False
        print("Exit")
    else:
        print("Sorry, I don't understand you, please try again.")
        continue
