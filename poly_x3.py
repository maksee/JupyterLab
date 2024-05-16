import numpy as np
import matplotlib.pyplot as plt

# Definicja funkcji
def funkcja(x):
    return (x - 1) * (x - 2) * (x - 3)

# Zakres wartości x
x = np.linspace(0.5, 3.5, 400)

# Wykres funkcji
plt.plot(x, funkcja(x), label='$(x-1)(x-2)(x-3)$')
plt.axhline(0, color='black', linewidth=0.5)  # Dodanie osi x
plt.axvline(0, color='black', linewidth=0.5)  # Dodanie osi y
plt.title('Wykres funkcji $(x-1)(x-2)(x-3)$')
plt.xlabel('x')
plt.ylabel('y')
plt.grid(True)
plt.legend()
plt.show()