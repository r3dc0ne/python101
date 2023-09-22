import matplotlib.pyplot as plt
import numpy as np

ky_sill = np.array([667, 762, 858, 953, 1048])
sil_and = np.array([1055, 935, 816, 697, 578])
and_ky = np.array([549, 709, 870, 1031, 1192])

pressure = np.array([1000, 3000, 5000, 7000, 9000])

fig, ax = plt.subplots()

ax.plot(ky_sill, pressure, label="ky-sill")
ax.plot(sil_and, pressure, label="sill-and")
ax.plot(and_ky, pressure, label="and-ky")

ax.set_xlabel('temperature [K]')
ax.set_ylabel('pressure [bar]')
ax.set_title('Sillimanite-Kyanite-Andesite')

ax.legend()

plt.show()
