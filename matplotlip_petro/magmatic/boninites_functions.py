
# for floats
def delete_rows_by_comparison(sheet_input, column_number, comparison_operator, comparison_value, start_row):
    for i in range(sheet_input.max_row, start_row, -1):
        cell_value = sheet_input.cell(row=i, column=column_number).value
        if cell_value is not None:
            cell_value = float(cell_value)
            if comparison_operator == '=' and cell_value == float(comparison_value):
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '>=' and cell_value >= float(comparison_value):
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '<=' and cell_value <= float(comparison_value):
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '>' and cell_value > float(comparison_value):
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '<' and cell_value < float(comparison_value):
                sheet_input.delete_rows(i, 1)
        else:
            sheet_input.delete_rows(i, 1)


# same for strings
def delete_rows_by_comparison_text(sheet_input, column_number, comparison_operator, comparison_value, start_row):
    for i in range(sheet_input.max_row, start_row, -1):
        cell_value = sheet_input.cell(row=i, column=column_number).value
        if cell_value is not None:
            # cell_value = float(cell_value)
            if comparison_operator == '=' and cell_value == comparison_value:
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '>=' and cell_value >= comparison_value:
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '<=' and cell_value <= comparison_value:
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '>' and cell_value > comparison_value:
                sheet_input.delete_rows(i, 1)
            elif comparison_operator == '<' and cell_value < comparison_value:
                sheet_input.delete_rows(i, 1)
        else:
            sheet_input.delete_rows(i, 1)


# get stuff
def get_all_rows_with_value(value, column_nr, sheet_output, sheet_input):
    row_counter = 2
    for i, row in enumerate(sheet_output.iter_rows(), start=1):
        if row[column_nr].value == value:
            for j, cell in enumerate(row, start=1):
                sheet_input.cell(row=row_counter, column=j, value=cell.value)
            row_counter += 1
        else:
            continue


# copy rows
def copy_row(sheet_out, row_nr_copy, sheet_in, row_nr_paste):
    """
    Copy a row from one sheet to another.

    Args:
        sheet_out (openpyxl.worksheet.Worksheet): The source worksheet.
        row_nr_copy (int): The row number to copy.
        sheet_in (openpyxl.worksheet.Worksheet): The destination worksheet.
        row_nr_paste (int): The row number to copy to.
    """
    # Iterate through the cells in the source row
    for col, cell in enumerate(sheet_out[row_nr_copy], start=1):
        # Read the value from the source cell
        value = cell.value

        # Write the value to the corresponding cell in the destination row
        sheet_in.cell(row=row_nr_paste, column=col, value=value)


# break

def filter_out_specific_rows(sheet_input, column_nr, value):
    for i in range(sheet_input.max_row, 0, -1):
        if sheet_input.cell(row=i, column=column_nr).value == value:
            sheet_input.delete_rows(i, 1)

    # column_nr is the cell in which the cluster numbers are (starts with 1)
        # example: column N --> column_nr = 14


def get_all_cells_from_citations(value_list, column_nr, sheet_output, sheet_input):
    for value in value_list:
        get_all_rows_with_value(value, column_nr, sheet_output, sheet_input)

# cluster_nr: user input
# column_nr is the cell in which the cluster numbers are - calculate minus 1 (starts with 0)
# example: column N --> column_nr = 13


def copy_specific_rows(sheet_output, sheet_input, row_start, row_end):
    for row in sheet_output.iter_rows(min_row=row_start):
        if row[0].row > row_end:
            break
        else:
            values = [cell.value for cell in row]
            sheet_input.append(values)


