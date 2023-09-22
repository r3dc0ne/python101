import numpy as np
import matplotlib.pyplot as plt
import mplstereonet

fig = plt.figure()
ax = fig.add_subplot(111, projection='stereonet')

# Define major and minor ticks
major_ticks = np.arange(0, 361, 20)
minor_ticks = np.arange(0, 361, 5)

# Set major and minor tick locations
ax.set_xticks(major_ticks)
ax.set_xticks(minor_ticks, minor=True)
ax.set_yticks(major_ticks)
ax.set_yticks(minor_ticks, minor=True)

# Set major and minor tick labels
ax.set_xticklabels(["N", "", "E", "", "S", "", "W", ""])
ax.set_yticklabels(["90", "", "60", "", "30", "", "0", "", "330", "", "300", "", "270", "", "240", "", "210", "", "180"])

# Set tick label font size
plt.xticks(fontsize=12)
plt.yticks(fontsize=12)

# Display grid
ax.grid(which='both')

# Show plot
plt.show()