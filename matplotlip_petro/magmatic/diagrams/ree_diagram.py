import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
from openpyxl import load_workbook
from helpful_functions import get_row_values, get_row_string_values

# izu-bonin boninites
workbook_ree_spidergram = load_workbook(
    filename="G:/My Drive/PycharmProjects/coding101/matplotlip_petro/magmatic/ree_spidergram.xlsx"
)
worksheet_ree = workbook_ree_spidergram["ree"]

list_all_rows = get_row_values(worksheet_ree, 4, 15)
list_x_axis = get_row_string_values(worksheet_ree, 1)

# Create a dictionary to map the string labels to numerical indices
label_to_index = {label: index for index, label in enumerate(list_x_axis)}

# Get the numerical indices for each label in the data
list_x_indices = [label_to_index[label] for label in list_x_axis]

# diagram plotter
plt.figure(figsize=(8, 4.5))

plt.axhline(y=0.1, color='grey', linestyle='-', linewidth=0.5, zorder=1)

AVAILABLE_COLORS = [
    "lightgreen",
    "lightblue",
    "salmon",
    "yellow",
    "orange",
    "purple",
    "lightgrey",
    "green",
    "grey",
    "blue",
    "pink",
    "red",
    "cyan",
    "magenta"
]

color_index = 0
for each_list in list_all_rows:
    plt.plot(list_x_axis, each_list, color=AVAILABLE_COLORS[color_index], zorder=2)
    plt.scatter(list_x_axis, each_list, color=AVAILABLE_COLORS[color_index], s=5, zorder=2)

    color_index += 1


plt.xlabel('REE')
plt.ylabel('REE occurrence in ppm')
plt.title('Rare Earth Element Diagram')

plt.xlim(-1, len(list_x_axis))
# plt.ylim(0, 0.5)

# Set the y-axis scale to logarithmic
plt.yscale('log')

# Set custom tick labels for logarithmic y-axis
y_ticks = [0.01, 0.1, 1, 10, 100, 1000]
y_tick_labels = ['0.01', '0.1', '1', '10', '100', '1000']
plt.gca().yaxis.set_major_locator(ticker.FixedLocator(y_ticks))
plt.gca().yaxis.set_major_formatter(ticker.FixedFormatter(y_tick_labels))
plt.gca().yaxis.set_minor_locator(ticker.NullLocator())

# plt.legend()
plt.savefig('ree_diagram.png', dpi=300)
plt.show()


# hochgestellt: \xb
# tiefgestellt: \u208
