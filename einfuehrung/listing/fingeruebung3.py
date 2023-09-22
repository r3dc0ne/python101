def sum_items(list_):
    first = 0
    for number in list_:
        first += number

    return first


bought_items = [3, 4.2, -1, 7]

print(sum_items(bought_items))

