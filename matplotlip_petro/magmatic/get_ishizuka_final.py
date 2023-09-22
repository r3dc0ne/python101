from openpyxl import load_workbook
from boninites_functions import delete_rows_by_comparison

workbook_ishizuka = load_workbook(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/boninites_ishizuka.xlsx"
)
sheet_to_delete = workbook_ishizuka["true_boninites"]
workbook_ishizuka.remove(sheet_to_delete)

sheet_ishizuka = workbook_ishizuka["ishizuka"]

delete_rows_by_comparison(sheet_ishizuka, 58, ">", 3, 1)

workbook_ishizuka.save(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/boninites_ishizuka_final.xlsx")
