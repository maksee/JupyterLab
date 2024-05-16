import numpy as np
import matplotlib.pyplot as plt

# Function definition
def function(x):
    return x**2 - 2

# Range of values x
x = np.linspace(-3, 3, 400)

# Graph of the function
plt.plot(x, function(x), label='$x^2 - 2$')
plt.axhline(0, color='black', linewidth=0.5)  # Adding x axis
plt.axvline(0, color='black', linewidth=0.5)  # Adding y axis
plt.title('Plot $x^2 - 2$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()