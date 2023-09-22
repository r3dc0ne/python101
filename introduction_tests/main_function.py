import random
from time import sleep


def sorted_list(amount_):
    lst = []
    for i in range(amount_):
        random_number = random.randint(1, 100)
        lst.append(random_number)
    lst.sort()
    length = len(lst)
    print("length: ", length)
    print(lst)

    return lst


def average_from_list(list_of_numbers, amount_):
    list_sum = sum(list_of_numbers)
    average = (list_sum / amount_)
    sleep(5)

    return average


def main():
    solution = average_from_list(sorted_list(amount), amount)

    return solution


amount = 10

if __name__ == "__main__":
    print("average: ", main())

