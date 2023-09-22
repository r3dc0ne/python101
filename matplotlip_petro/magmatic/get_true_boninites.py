from openpyxl import load_workbook
from boninites_functions import delete_rows_by_comparison

workbook_boninites = load_workbook(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/boninites_excel.xlsx"
)
sheet_original = workbook_boninites["original"]

delete_rows_by_comparison(sheet_original, 28, "<", float(52), 1)
delete_rows_by_comparison(sheet_original, 28, ">", float(63), 1)
delete_rows_by_comparison(sheet_original, 37, "<=", float(8), 1)
delete_rows_by_comparison(sheet_original, 29, ">=", float(0.5), 1)

workbook_boninites.save(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/true_boninites.xlsx"
)
