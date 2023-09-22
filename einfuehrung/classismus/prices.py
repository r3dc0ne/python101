def get_mineral_price_info_from_file(file_name):
    file_handle = open(file_name, "r")
    file_lines = file_handle.readlines()
    file_handle.close()
    file_lines.pop(0)
    return file_lines


def get_mineral_prices():
    prices_dict = {}
    for mineral_info in get_mineral_price_info_from_file("mineral_prices.csv"):
        single_info = mineral_info.split(";")
        mineral_type = single_info[0].upper()
        mineral_price = int(single_info[1])
        prices_dict[mineral_type] = mineral_price

    return prices_dict


PRICES = get_mineral_prices()
