import matplotlib.pyplot as plt

# Generate some data
x = [1, 2, 3, 4, 5]
y = [10, 100, 1000, 10000, 100000]

# Create a plot
plt.plot(x, y)

# Set the y-axis scale to logarithmic
plt.yscale('log')

# Show the plot
plt.show()
