class Person:
    def __init__(self, name, likes_persons):
        self.name = name
        self.answer = ""
        self.mood = ""
        self.likes_persons = likes_persons

    def get_name(self):
        return self.name

    def set_mood(self, mood):
        self.mood = mood

    def get_mood(self):
        return self.mood

    def ask_to_prom(self, person):

        if self.get_name() in person.likes_persons:
            if person.likes_persons[self.get_name()] >= 9:
                person.set_answer("yes")
                return

        person.set_answer("no")

    def set_answer(self, answer):
        self.answer = answer

    def get_answer(self):
        return self.answer


if __name__ == "__main__":
    dorina = Person("Butterbluemchen", {"Morgentautroepfchen": 10})
    anna = Person("Morgentautroepfchen", {"Butterbluemchen": 10, "bison": 3})

    dorina.ask_to_prom(anna)

    if anna.get_answer() == "yes":
        dorina.set_mood("happy")
    else:
        dorina.set_mood("sad")

    print(anna.get_name(), "said", anna.get_answer(), "so", dorina.get_name(), "is", dorina.get_mood())
