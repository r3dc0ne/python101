import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
from helpful_functions import get_column_values, salters_stracke

# true boninites
workbook_true_boninites = load_workbook(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/boninites_ishizuka_final.xlsx"
)
worksheet_mg_nd = workbook_true_boninites["mg_number_epsilon_nd"]

list_epsilon_Nd = get_column_values(worksheet_mg_nd, 1)
list_Mg_number = get_column_values(worksheet_mg_nd, 2)

# diagram plotter
plt.figure(figsize=(8, 6))

plt.scatter(list_epsilon_Nd, list_Mg_number, color="blue", s=10, label="Izu-Bonin Boninites", zorder=2)


plt.xlabel('Mg#')
plt.ylabel('\u03B5Nd')
plt.title('\u03B5Nd over Mg#')

#plt.xlim(0.5108, 0.5133)
#plt.ylim(0.2827, 0.2834)

plt.legend()
plt.savefig('mg_nd.png', dpi=300)
plt.show()



# hochgestellt: \xb
# tiefgestellt: \u208
