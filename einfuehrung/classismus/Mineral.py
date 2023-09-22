from prices import PRICES


class Mineral:

    def __init__(self, weight, mineral_type, notes):
        self.weight = weight
        self.mineral_type = mineral_type
        self.notes = notes
        self.__value = self.calculate_value()

    def __str__(self):
        return self.get_mineral_string()

    def __repr__(self):
        return self.get_mineral_string()

    def get_mineral_string(self):
        mineral = "{}{}{}{}".format(
            str(self.weight).ljust(6, " "),
            self.mineral_type.ljust(10, " "),
            self.notes.ljust(20, " "),
            str(self.__value).rjust(7, " ")
        )

        return mineral

    def get_mineral_type(self):
        return str(self.mineral_type)

    def get_mineral_value(self):
        return self.__value

    def calculate_value(self):
        mineral_type = self.get_mineral_type()
        value = PRICES[mineral_type.upper()]
        return self.weight * value

