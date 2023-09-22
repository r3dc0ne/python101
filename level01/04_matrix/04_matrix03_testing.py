import random


def random_number_2(amount):
    second_random_number = random.randrange(len(amount))
    temp_list_random_number = list(amount)
    temp_list_hashtags = "".join(temp_list_random_number)
    return second_random_number


def random_number_1(how_many):
    temp_list = how_many * hashtags_list
    first_random_number = random.randrange(len(temp_list))
    return first_random_number


def list_of_numbers(amount_randoms):
    number_list = []

    for i in range(amount_randoms):
        number_list.append(random_number_2(hashtags))
        number_list.append(random_number_1(height))
        number_list.append('')  # das ist nur zur orientierung

    print(number_list)


# hier ist jetzt folgendes problem:
# ich kann ja bei der jeweiligen random_number schon Doppelungen haben, nur nicht bei der Kombination
    # damit hinterher bei der Matrix keine Stelle doppelt besetzt wird
# deshalb kam ich dann darauf die irgendwie aneinander zu "binden"
    # dann wieder in eine Liste zu packen
    # und dann zu vergleichen, ob es Doppelungen gibt usw.
# und dann hab ich gedacht, naja das sind dann ja so zahlen wie 12, 43, 25 usw.
    # warum mach ich das nicht alles in einer Linie, statt in zwei dimensionen zu denken mit random_number 1 und 2
        # dann fiel mir ein, dass
            # dodo das so gemacht hat
            # und ich müsste meinen ganzen code wieder umschreiben
        # und ich möchte erstmal eine loesung mit meinem eigenen code finden

        # siehe listing für weiteres!!!!

width = 5
height = 5
randoms = 5

hashtags = "#" * width
hashtags_list = [hashtags]

list_of_numbers(randoms)

