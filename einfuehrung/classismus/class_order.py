class Printy:
    def __init__(self, text=""):
        self.text = text

    def do_print(self):
        print(self.text)

    def __repr__(self):
        return self.text


list_of_text = []

list_of_text.append(Printy("Cranberry"))
list_of_text.append(Printy("Cashew"))
list_of_text.append(Printy("Mix"))
list_of_text.append(Printy("Nudeln"))


for element in reversed(list_of_text):
    element.do_print()


