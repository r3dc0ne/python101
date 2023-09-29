class Person:
    def __init__(self, name):
        self.name = name

    def get_name(self):
        return self.name


class Anna(Person):
    def __init__(self, name):
        super().__init__(name)
        self.answer = ""

    def set_answer(self, answer):
        self.answer = answer

    def get_answer(self):
        return self.answer


class Dorina(Person):
    def __init__(self, name):
        super().__init__(name)
        self.mood = ""

    def set_mood(self, mood):
        self.mood = mood

    def get_mood(self):
        return self.mood

    @staticmethod
    def ask_to_prom(anna: Anna):
        anna.set_answer("yes")


if __name__ == "__main__":
    dorina = Dorina("Butterbluemchen")
    anna = Anna("Morgentautroepfchen")

    dorina.ask_to_prom(anna)

    if anna.get_answer() == "yes":
        dorina.set_mood("happy")
    else:
        dorina.set_mood("sad")

    print(anna.get_name(), "said", anna.get_answer(), "so", dorina.get_name(), "is", dorina.get_mood())
