import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
from helpful_functions import get_column_values, salters_stracke

# true boninites
workbook_true_boninites = load_workbook(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/boninites_ishizuka_final.xlsx"
)
worksheet_true = workbook_true_boninites["ishizuka"]

list_Nd = get_column_values(worksheet_true, 147)
list_Sr = get_column_values(worksheet_true, 150)

# diagram plotter
plt.figure(figsize=(8, 6))

plt.axvline(x=salters_stracke("BSE", "Sr"), color='grey', linestyle='-', linewidth=0.5, zorder=1)
plt.axhline(y=salters_stracke("BSE", "Nd"), color='grey', linestyle='-', linewidth=0.5, zorder=1)

plt.scatter(list_Sr, list_Nd, color="red", s=10, label="Izu-Bonin Boninites", zorder=2)
plt.scatter(salters_stracke("DM", "Sr"), salters_stracke("DM", "Nd"),
            color="blue", s=10, label="Depleted Mantle", zorder=2
            )
plt.scatter(salters_stracke("BSE", "Sr"), salters_stracke("BSE", "Nd"),
            color="green", s=10, label="Bulk Silikate Earth", zorder=2
            )
plt.scatter(salters_stracke("EM1", "Sr"), salters_stracke("EM1", "Nd"),
            color="orange", s=10, label="Enriched Mantle 1", zorder=2
            )
plt.scatter(salters_stracke("EM2", "Sr"), salters_stracke("EM2", "Nd"),
            color="purple", s=10, label="Enriched Mantle 2", zorder=2
            )

plt.text(0.7055, 0.51295, s="Izu-Bonin Boninites", fontsize=8)
plt.text(salters_stracke("DM", "Sr")-0.0011, salters_stracke("DM", "Nd"), s="DM", fontsize=8)
plt.text(salters_stracke("BSE", "Sr")-0.0011, salters_stracke("BSE", "Nd")+0.00002, s="BSE", fontsize=8)
plt.text(salters_stracke("EM1", "Sr")+0.0003, salters_stracke("EM1", "Nd")-0.00004, s="EM1", fontsize=8)
plt.text(salters_stracke("EM2", "Sr")+0.0003, salters_stracke("EM2", "Nd")-0.00004, s="EM2", fontsize=8)

plt.plot([salters_stracke("DM", "Sr"), salters_stracke("EM2", "Sr")],
         [salters_stracke("DM", "Nd"), salters_stracke("EM2", "Nd")],
         color='lightgrey',
         linestyle="--",
         linewidth=0.5,
         zorder=1
         )

plt.xlabel('$^{87}$Sr/$^{86}$Sr')
plt.ylabel('$^{143}$Nd/$^{144}$Nd')
plt.title('$^{143}$Nd/$^{144}$Nd over $^{87}$Sr/$^{86}$Sr')

plt.xlim(0.7, 0.725)
plt.ylim(0.5108, 0.5133)

# plt.legend()
plt.savefig('nd_sr.png', dpi=300)
plt.show()


# hochgestellt: \xb
# tiefgestellt: \u208
