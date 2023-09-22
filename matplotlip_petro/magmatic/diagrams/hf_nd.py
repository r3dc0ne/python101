import matplotlib.pyplot as plt
import numpy as np
from openpyxl import load_workbook
from helpful_functions import get_column_values, salters_stracke

# true boninites
workbook_true_boninites = load_workbook(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/boninites_ishizuka_final.xlsx"
)
worksheet_true = workbook_true_boninites["ishizuka"]

list_Hf = get_column_values(worksheet_true, 164)
list_Nd = get_column_values(worksheet_true, 147)

# diagram plotter
plt.figure(figsize=(8, 6))

plt.axvline(x=salters_stracke("BSE", "Nd"), color='grey', linestyle='-', linewidth=0.5, zorder=1)
plt.axhline(y=salters_stracke("BSE", "Hf"), color='grey', linestyle='-', linewidth=0.5, zorder=1)

plt.scatter(list_Nd, list_Hf, color="red", s=10, label="Izu-Bonin Boninites", zorder=2)
plt.scatter(salters_stracke("DM", "Nd"), salters_stracke("DM", "Hf"),
            color="blue", s=10, zorder=2
            )
plt.scatter(salters_stracke("BSE", "Nd"), salters_stracke("BSE", "Hf"),
            color="green", s=10, zorder=2
            )
plt.scatter(salters_stracke("EM1", "Nd"), salters_stracke("EM1", "Hf"),
            color="orange", s=10, zorder=2
            )
plt.scatter(salters_stracke("EM2", "Nd"), salters_stracke("EM2", "Hf"),
            color="purple", s=10, zorder=2
            )

plt.plot([salters_stracke("DM", "Nd"),
          ((salters_stracke("EM2", "Nd")-salters_stracke("EM1", "Nd"))/2)+salters_stracke("EM1", "Nd")
          ],
         [salters_stracke("DM", "Hf"),
          ((salters_stracke("EM2", "Hf")-salters_stracke("EM1", "Hf"))/2)+salters_stracke("EM1", "Hf")
          ],
         color='lightgrey', linestyle="--", linewidth=0.5, zorder=1
         )

plt.xlabel('$^{143}$Nd/$^{144}$Nd')
plt.ylabel('$^{176}$Hf/$^{177}$Hf')
plt.title('$^{176}$Hf/$^{177}$Hf over $^{143}$Nd/$^{144}$Nd')

plt.text(0.5128, 0.2831, s="Izu-Bonin Boninites", fontsize=8)
plt.text(salters_stracke("DM", "Nd")+0.00004, salters_stracke("DM", "Hf"), s="DM", fontsize=8)
plt.text(salters_stracke("BSE", "Nd")+0.00004, salters_stracke("BSE", "Hf")+0.00001, s="BSE", fontsize=8)
plt.text(salters_stracke("EM1", "Nd")+0.00004, salters_stracke("EM1", "Hf"), s="EM1", fontsize=8)
plt.text(salters_stracke("EM2", "Nd")+0.00004, salters_stracke("EM2", "Hf"), s="EM2", fontsize=8)


plt.xlim(0.5108, 0.5133)
plt.ylim(0.2827, 0.2834)

# plt.legend()
plt.savefig('hf_nd.png', dpi=300)
plt.show()



# hochgestellt: \xb
# tiefgestellt: \u208
