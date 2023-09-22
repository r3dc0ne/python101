import numpy as np
import mplstereonet
import matplotlib.pyplot as plt
import FaultMeasure

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


def plot_data(data_list, safe_file_name=None):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='stereonet')

    # ax.set_yticks(np.deg2rad([0, 90, 180, 270]))
    # ax.set_yticklabels(['N', 'E', 'S', 'W'])

    #ax.set_xticks([0, np.pi / 2, np.pi, 3 * np.pi / 2])
    #ax.set_yticks([0, np.pi / 2, np.pi, 3 * np.pi / 2])

    #ax.set_xticklabels(['N', 'E', 'S', 'W'])
    #ax.set_yticklabels(['N', 'E', 'S', 'W'])

    color_index = 0
    for fault_measure in data_list:

        ax.plane(
            fault_measure.strike,
            fault_measure.dip,
            label='Fault %03d/%02d' % (fault_measure.strike, fault_measure.dip),
            color=AVAILABLE_COLORS[color_index]
        )

        ax.rake(
            fault_measure.strike,
            fault_measure.dip,
            fault_measure.plunge,
            markersize=10,
            color="green"
        )

        # ax.legend()
        # ax.legend(loc='upper right')
        ax.legend(loc=(0.7, 0.7))

        color_index += 1

        """plunge, bearing = mplstereonet.plane_intersection(strike1, dip1, strike2, dip2)
        ax.line(plunge, bearing, 'ko', markersize=5,
                label='Intersection %02d/%03d' % (plunge, bearing))"""
    ax.legend()
    # We can also add a grid
    # ax.grid()

    """# Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(0, 101, 20)
    minor_ticks = np.arange(0, 101, 5)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    # And a corresponding grid
    ax.grid(which='both')

    # Or if you want different settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)"""

    if safe_file_name is None:
        plt.show()

    else:
        pass
        # TODO: safe to file here


if __name__ == "__main__":
    full_csv_file = open("old_dolling_fault.csv", "r").read()
    csv_lines = full_csv_file.split("\n")
    all_data = []
    for line in csv_lines:
        all_data.append(FaultMeasure.FaultMeasure(line.split(";")))

    plot_data(all_data)
