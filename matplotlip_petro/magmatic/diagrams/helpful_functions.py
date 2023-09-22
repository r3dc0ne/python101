# get values out of a specific column (for loop starts with row 2)
def get_column_values(data_sheet, column_number):
    column_values = []
    for row in data_sheet.iter_rows(min_row=2, min_col=column_number, max_col=column_number):
        for cell in row:
            column_values.append(cell.value)

    return column_values

    # column number starts with 1


# sum values of two lists and make a new list
def sum_two_lists(list_1, list_2):
    result_list = []
    for i in range(len(list_1)):
        if list_1[i] is None or list_2[i] is None:
            if list_1[i] is None and list_2[i] is not None:
                sum_value = list_2[i]
            elif list_2[i] is None and list_1[i] is not None:
                sum_value = list_1[i]
            else:
                sum_value = 0
        else:
            sum_value = list_1[i] + list_2[i]
        result_list.append(sum_value)

    return result_list


def get_row_values(worksheet, min_row, max_row):
    list_of_row_lists = []

    for row in worksheet.iter_rows(min_row=min_row, max_row=max_row, values_only=True):
        list_current_row = []
        for cell in row:
            list_current_row.append(cell)
        list_of_row_lists.append(list_current_row)

    return list_of_row_lists


def get_row_string_values(worksheet, row_index):
    row = worksheet[row_index]
    return [str(cell.value) for cell in row]


def salters_stracke(setting, element):
    global isotope_value
    if setting == "DM":
        if element == "Sr":
            isotope_value = 0.7026
        elif element == "Nd":
            isotope_value = 0.51311
        elif element == "Hf":
            isotope_value = 0.2833
    elif setting == "BSE":
        if element == "Sr":
            isotope_value = 0.7045
        elif element == "Nd":
            isotope_value = 0.512634
        elif element == "Hf":
            isotope_value = 0.282843
    elif setting == "EM1":
        if element == "Sr":
            isotope_value = 0.705
        elif element == "Nd":
            isotope_value = 0.5112
        elif element == "Hf":
            isotope_value = 0.28274
    elif setting == "EM2":
        if element == "Sr":
            isotope_value = 0.722
        elif element == "Nd":
            isotope_value = 0.511
        elif element == "Hf":
            isotope_value = 0.282816

    return isotope_value


