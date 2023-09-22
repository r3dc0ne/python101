from Mineral import Mineral
import csv


def get_mineral_info_from_file(file_name):
    file_handle = open(file_name, "r")
    file_lines = file_handle.readlines()
    file_handle.close()
    file_lines.pop(0)
    return file_lines


def get_header_from_file(file_name):
    file_handle = open(file_name, "r")
    header_line = file_handle.readline().rstrip()
    file_handle.close()
    headers = header_line.split(";")
    header = "{}{}{}{}".format(
        headers[0].ljust(6, " "),
        headers[1].ljust(10, " "),
        headers[2].ljust(20, " "),
        "value".rjust(7, " ")
    )

    return header


def get_minerals_list(mineral_infos):
    minerals_list = []
    for mineral_info in mineral_infos:
        single_info = mineral_info.split(";")
        mineral_weight = int(single_info[0])
        mineral_type = single_info[1]
        mineral_note = single_info[2].rstrip()
        current_mineral = Mineral(mineral_weight, mineral_type, mineral_note)
        minerals_list.append(current_mineral)

    return minerals_list


def get_sum_prices(all_minerals):
    sum_prices = 0
    for mineral in all_minerals:
        sum_prices += mineral.get_mineral_value()

    return sum_prices


def print_minerals(minerals):

    for mineral in minerals:
        print(str(mineral))


if __name__ == "__main__":
    mineral_info_list = get_mineral_info_from_file("minerals.csv")
    minerals_list = get_minerals_list(mineral_info_list)
    print(get_header_from_file("minerals.csv"))
    print_minerals(minerals_list)
    print(str(get_sum_prices(minerals_list)).rjust(43, " "))


